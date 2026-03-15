{% extends "base.html" %}
{% block title %}BiteLocal - Find Local Restaurants{% endblock %}

{% block content %}

<!-- Hero -->
<section class="hero">
    <div class="hero-text">
        <h2>Find the Best<br>Local Restaurants<br>Near You 🍕</h2>
        <p>Discover hidden gems, read real reviews, save your favorites, and find the best deals at local restaurants in Louisville.</p>
        <div class="hero-btns">
            <a href="{{ url_for('browse') }}" class="btn btn-red">Browse Restaurants</a>
            <a href="{{ url_for('deals') }}"  class="btn btn-outline">🏷️ See All Deals</a>
        </div>
    </div>
    <div class="hero-stats">
        <div class="stat-box"><span class="stat-num">{{ restaurants|length }}</span><span class="stat-label">Restaurants</span></div>
        <div class="stat-box"><span class="stat-num">5</span><span class="stat-label">Categories</span></div>
        <div class="stat-box"><span class="stat-num">100%</span><span class="stat-label">Local</span></div>
    </div>
</section>

<!-- ══ DEALS SLIDESHOW ══ -->
<section class="deals-section">
    <h2>🏷️ Today's Hot Deals</h2>
    <p class="deals-sub">Click any deal to visit the restaurant and claim it!</p>

    <div class="slideshow-wrapper">
        <button class="slide-arrow left-arrow" onclick="moveSlide(-1)">&#8249;</button>

        <div class="slideshow-track" id="slideshowTrack">
            {% for r in restaurants %}
            <div class="deal-slide">
                <a href="{{ url_for('detail', restaurant_id=r.id) }}" class="deal-slide-inner {{ r.category }}">
                    <img src="{{ r.img }}" alt="{{ r.name }}">
                    <div class="deal-slide-info">
                        <span class="deal-cat-badge">{{ r.category|title }}</span>
                        <h3>{{ r.name }}</h3>
                        <div class="deal-tag">🏷️ {{ r.deal }}</div>
                        <div class="deal-code-box">
                            Code: <strong>{{ r.deal_code }}</strong>
                        </div>
                        <p class="deal-loc">📍 {{ r.location }}</p>
                        <span class="deal-cta">Tap to Claim →</span>
                    </div>
                </a>
            </div>
            {% endfor %}
        </div>

        <button class="slide-arrow right-arrow" onclick="moveSlide(1)">&#8250;</button>
    </div>

    <!-- dots -->
    <div class="slide-dots" id="slideDots">
        {% for r in restaurants %}
        <button class="dot {{ 'active' if loop.first }}" onclick="goToSlide({{ loop.index0 }})"></button>
        {% endfor %}
    </div>

    <div style="text-align:center; margin-top:20px;">
        <a href="{{ url_for('deals') }}" class="btn btn-red">View All {{ restaurants|length }} Deals</a>
    </div>
</section>

<!-- Category cards -->
<section class="home-categories">
    <h2>Browse by Food Type</h2>
    <div class="cat-grid">
        <a href="{{ url_for('browse', category='american') }}" class="cat-card american">
            <span>🍔</span><h3>American</h3><p>Burgers, BBQ, Diners</p>
        </a>
        <a href="{{ url_for('browse', category='italian') }}" class="cat-card italian">
            <span>🍝</span><h3>Italian</h3><p>Pasta, Pizza, More</p>
        </a>
        <a href="{{ url_for('browse', category='asian') }}" class="cat-card asian">
            <span>🍜</span><h3>Asian</h3><p>Sushi, Pho, Chinese</p>
        </a>
        <a href="{{ url_for('browse', category='mexican') }}" class="cat-card mexican">
            <span>🌮</span><h3>Mexican</h3><p>Tacos, Burritos, More</p>
        </a>
        <a href="{{ url_for('browse', category='desserts') }}" class="cat-card desserts">
            <span>🍦</span><h3>Desserts</h3><p>Ice Cream & Sweets</p>
        </a>
    </div>
</section>

<!-- Features -->
<section class="features">
    <h2>What You Can Do</h2>
    <div class="features-grid">
        <a href="{{ url_for('browse') }}" class="feature">
            <span>🔍</span><h3>Search & Filter</h3><p>Find restaurants by name, food type, or location</p>
        </a>
        <a href="{{ url_for('browse') }}" class="feature">
            <span>⭐</span><h3>Leave Reviews</h3><p>Rate restaurants and share your experience</p>
        </a>
        <a href="{{ url_for('bookmarks_page') }}" class="feature">
            <span>🔖</span><h3>Save Favorites</h3><p>Bookmark restaurants you want to visit</p>
        </a>
        <a href="{{ url_for('deals') }}" class="feature">
            <span>🏷️</span><h3>Find Deals</h3><p>Every restaurant has a special deal or coupon</p>
        </a>
        <a href="{{ url_for('submit') }}" class="feature">
            <span>➕</span><h3>Add a Restaurant</h3><p>Know a great spot? Submit it to our directory</p>
        </a>
        <a href="{{ url_for('report') }}" class="feature">
            <span>📊</span><h3>View Report</h3><p>See stats, top rated spots, and data</p>
        </a>
    </div>
</section>

<!-- Slideshow JS -->
<script>
    let currentSlide = 0;
    const track = document.getElementById("slideshowTrack");
    const dots   = document.querySelectorAll(".dot");

    // how many slides fit visible at once (show 3 at a time on desktop)
    function visibleCount() {
        return window.innerWidth < 700 ? 1 : window.innerWidth < 1000 ? 2 : 3;
    }

    function totalSlides() {
        return track.children.length;
    }

    function updateSlide() {
        const slideWidth = track.children[0].offsetWidth + 20; // 20 = gap
        track.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
        dots.forEach((d, i) => d.classList.toggle("active", i === currentSlide));
    }

    function moveSlide(dir) {
        const max = totalSlides() - visibleCount();
        currentSlide = Math.max(0, Math.min(currentSlide + dir, max));
        updateSlide();
    }

    function goToSlide(n) {
        const max = totalSlides() - visibleCount();
        currentSlide = Math.min(n, max);
        updateSlide();
    }

    // auto-advance every 3 seconds
    setInterval(() => {
        const max = totalSlides() - visibleCount();
        currentSlide = currentSlide >= max ? 0 : currentSlide + 1;
        updateSlide();
    }, 3000);

    window.addEventListener("resize", updateSlide);
</script>

{% endblock %}
