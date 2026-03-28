<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ethio-Connect | Verified Ethiopian Dating Ecosystem Research</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #1a1a2e;
            --secondary: #16213e;
            --accent: #e94560;
            --gold: #d4af37;
            --green: #2ecc71;
            --text: #f1f1f1;
            --text-muted: #a0a0a0;
            --gradient-1: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            --gradient-2: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
            --glass: rgba(255, 255, 255, 0.05);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--primary);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }

        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: var(--primary);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--accent);
            border-radius: 5px;
        }

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 1.5rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            background: rgba(26, 26, 46, 0.9);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--gold);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: var(--text);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
            position: relative;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--accent);
            transition: width 0.3s;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-links a:hover {
            color: var(--accent);
        }

        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 120px 5% 80px;
            background: var(--gradient-1);
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(233, 69, 96, 0.15) 0%, transparent 70%);
            animation: pulse 8s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 0.8; }
        }

        .hero-content {
            max-width: 900px;
            text-align: center;
            z-index: 1;
        }

        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #fff 0%, var(--gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: fadeInUp 1s ease;
        }

        .hero-subtitle {
            font-size: 1.3rem;
            color: var(--text-muted);
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease 0.2s both;
        }

        .hero-description {
            font-size: 1.1rem;
            color: var(--text);
            margin-bottom: 3rem;
            line-height: 1.8;
            animation: fadeInUp 1s ease 0.4s both;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            animation: fadeInUp 1s ease 0.6s both;
        }

        .btn {
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn-primary {
            background: var(--gradient-2);
            color: white;
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(233, 69, 96, 0.4);
        }

        .btn-secondary {
            background: transparent;
            color: var(--text);
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: var(--accent);
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        section {
            padding: 100px 5%;
            position: relative;
        }

        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-header h2 {
            font-family: 'Playfair Display', serif;
            font-size: 2.8rem;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        .section-header p {
            color: var(--text-muted);
            max-width: 600px;
            margin: 0 auto;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .card {
            background: var(--glass);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: var(--gradient-2);
            transform: scaleX(0);
            transition: transform 0.3s;
        }

        .card:hover::before {
            transform: scaleX(1);
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            border-color: rgba(233, 69, 96, 0.3);
        }

        .card-icon {
            font-size: 2.5rem;
            color: var(--accent);
            margin-bottom: 1rem;
        }

        .card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: white;
        }

        .card p {
            color: var(--text-muted);
            line-height: 1.8;
        }

        .table-container {
            max-width: 1200px;
            margin: 0 auto;
            overflow-x: auto;
            background: var(--glass);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            background: rgba(233, 69, 96, 0.2);
            color: var(--gold);
            padding: 1.2rem;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid var(--accent);
        }

        td {
            padding: 1.2rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            color: var(--text);
        }

        tr:hover td {
            background: rgba(255, 255, 255, 0.02);
        }

        .tech-specs {
            background: var(--secondary);
        }

        .spec-item {
            display: flex;
            gap: 1.5rem;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 15px;
            border-left: 4px solid var(--accent);
        }

        .spec-number {
            font-size: 2rem;
            font-weight: 700;
            color: var(--accent);
            min-width: 50px;
        }

        .spec-content h4 {
            color: var(--gold);
            margin-bottom: 0.5rem;
        }

        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .pricing-card {
            background: var(--glass);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2.5rem 2rem;
            text-align: center;
            position: relative;
            transition: all 0.3s;
        }

        .pricing-card.featured {
            border-color: var(--gold);
            transform: scale(1.05);
        }

        .pricing-card.featured::before {
            content: 'POPULAR';
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--gold);
            color: var(--primary);
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
        }

        .pricing-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .pricing-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: var(--text);
        }

        .price {
            font-size: 3rem;
            font-weight: 700;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }

        .price span {
            font-size: 1rem;
            color: var(--text-muted);
        }

        .features {
            list-style: none;
            margin: 2rem 0;
            text-align: left;
        }

        .features li {
            padding: 0.5rem 0;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .features li i {
            color: var(--green);
        }

        .compliance-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .compliance-card {
            background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(46, 204, 113, 0.05) 100%);
            border: 1px solid rgba(46, 204, 113, 0.2);
            border-radius: 15px;
            padding: 2rem;
        }

        .compliance-card h4 {
            color: var(--green);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .cultural-section {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, transparent 100%);
        }

        .cultural-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .cultural-card {
            background: rgba(212, 175, 55, 0.05);
            border: 1px solid rgba(212, 175, 55, 0.2);
            border-radius: 15px;
            padding: 2rem;
            position: relative;
        }

        .cultural-card::after {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, transparent 50%, rgba(212, 175, 55, 0.2) 50%);
            border-radius: 0 15px 0 0;
        }

        .roadmap {
            max-width: 1000px;
            margin: 0 auto;
            position: relative;
        }

        .roadmap::before {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 100%;
            background: linear-gradient(to bottom, var(--accent), var(--gold));
        }

        .roadmap-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4rem;
            position: relative;
        }

        .roadmap-item:nth-child(even) {
            flex-direction: row-reverse;
        }

        .roadmap-content {
            width: 45%;
            background: var(--glass);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .roadmap-dot {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 20px;
            background: var(--accent);
            border-radius: 50%;
            border: 4px solid var(--primary);
        }

        .roadmap-number {
            font-size: 3rem;
            font-weight: 700;
            color: var(--accent);
            opacity: 0.3;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            top: -20px;
        }

        footer {
            background: var(--secondary);
            padding: 60px 5% 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-section h4 {
            color: var(--gold);
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
        }

        .footer-section ul {
            list-style: none;
        }

        .footer-section ul li {
            margin-bottom: 0.8rem;
        }

        .footer-section a {
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-section a:hover {
            color: var(--accent);
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-muted);
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .nav-links {
                display: none;
            }
            
            .roadmap::before {
                left: 20px;
            }
            
            .roadmap-item {
                flex-direction: column !important;
                align-items: flex-start;
                padding-left: 50px;
            }
            
            .roadmap-content {
                width: 100%;
            }
            
            .roadmap-dot {
                left: 20px;
            }
            
            .pricing-card.featured {
                transform: scale(1);
            }
        }

        .highlight-box {
            background: rgba(233, 69, 96, 0.1);
            border-left: 4px solid var(--accent);
            padding: 1.5rem;
            margin: 2rem 0;
            border-radius: 0 10px 10px 0;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 1000px;
            margin: 3rem auto;
        }

        .stat-item {
            text-align: center;
            padding: 2rem;
            background: var(--glass);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 700;
            color: var(--accent);
            display: block;
        }

        .stat-label {
            color: var(--text-muted);
            margin-top: 0.5rem;
        }

        .code-block {
            background: #0d1117;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .code-block .comment { color: #8b949e; }
        .code-block .keyword { color: #ff7b72; }
        .code-block .string { color: #a5d6ff; }
        .code-block .function { color: #d2a8ff; }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <a href="#" class="logo">
            <i class="fas fa-heart"></i>
            Ethio-Connect
        </a>
        <ul class="nav-links">
            <li><a href="#overview">Overview</a></li>
            <li><a href="#competition">Competition</a></li>
            <li><a href="#biometric">Biometrics</a></li>
            <li><a href="#location">Location</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#compliance">Compliance</a></li>
            <li><a href="#roadmap">Roadmap</a></li>
        </ul>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Verified Ethiopian Dating Ecosystems</h1>
            <p class="hero-subtitle">Architectural and Strategic Framework Research</p>
            <p class="hero-description">
                A comprehensive analysis of trust-first digital transformation in Ethiopia's relationship sector. 
                Addressing the critical "Trust Deficit" through biometric verification, Fayda National ID integration, 
                and culturally-aligned matchmaking algorithms.
            </p>
            <div class="cta-buttons">
                <a href="#overview" class="btn btn-primary">
                    <i class="fas fa-book-open"></i>
                    Read Research
                </a>
                <a href="#roadmap" class="btn btn-secondary">
                    <i class="fas fa-code"></i>
                    Technical Specs
                </a>
            </div>
        </div>
    </section>

    <!-- Overview Section -->
    <section id="overview">
        <div class="section-header">
            <h2>Executive Summary</h2>
            <p>The digital transformation of social interaction in Ethiopia represents one of the most significant socio-technical shifts in the Horn of Africa.</p>
        </div>

        <div class="highlight-box">
            <strong><i class="fas fa-exclamation-triangle"></i> The Trust Deficit:</strong> 
            Market research indicates that users frequently encounter fraudulent profiles, financial scams, and individuals with ambiguous motives, 
            often colloquially referred to as "ferenji hunting" or "gold digging".
        </div>

        <div class="stat-grid">
            <div class="stat-item">
                <span class="stat-number">400K+</span>
                <div class="stat-label">Gojo App Users</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">99.8%</span>
                <div class="stat-label">Smile ID Accuracy</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">90M</span>
                <div class="stat-label">Fayda ID Goal by 2028</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">500K</span>
                <div class="stat-label">ETB PDPP Penalty</div>
            </div>
        </div>

        <div class="cards-grid">
            <div class="card">
                <div class="card-icon"><i class="fas fa-shield-alt"></i></div>
                <h3>Verification-First Methodology</h3>
                <p>Government-linked database confirmation, biometric liveness detection, and network-based location validation to ensure authentic self-representation.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-mobile-alt"></i></div>
                <h3>Mobile-Money Integration</h3>
                <p>Seamless Telebirr and CBE Birr integration for daily, weekly, and monthly subscription tiers catering to diverse income levels.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-globe-africa"></i></div>
                <h3>Cultural Alignment</h3>
                <p>Marriage-oriented connections respecting traditional social values while leveraging modern mobile technology.</p>
            </div>
        </div>
    </section>

    <!-- Competitive Analysis -->
    <section id="competition" style="background: var(--secondary);">
        <div class="section-header">
            <h2>Competitive Analysis</h2>
            <p>Market positioning against existing Ethiopian dating platforms</p>
        </div>

        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Platform</th>
                        <th>Target Demographic</th>
                        <th>Verification Method</th>
                        <th>Monetization Model</th>
                        <th>Unique Value Proposition</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Gojo</strong></td>
                        <td>Habesha singles (Global)</td>
                        <td>Blue checkmark, phone/email</td>
                        <td>Tiered Platinum/Gold/Silver</td>
                        <td>Largest community, religion filters</td>
                    </tr>
                    <tr>
                        <td><strong>Maraki</strong></td>
                        <td>Local Ethiopian singles</td>
                        <td>Photo upload, manual review</td>
                        <td>Subscription & In-app gifts</td>
                        <td>Integrated relationship counseling</td>
                    </tr>
                    <tr>
                        <td><strong>Ethio Marriage</strong></td>
                        <td>Marriage-focused locals</td>
                        <td>Identity-first avatars</td>
                        <td>Premium month-long access</td>
                        <td>Personality-first, HIV status info</td>
                    </tr>
                    <tr>
                        <td><strong>KumNeger</strong></td>
                        <td>Diaspora & Serious seekers</td>
                        <td>Phone number registration</td>
                        <td>Freemium with month-long trial</td>
                        <td>Strong Eritrean community connection</td>
                    </tr>
                    <tr>
                        <td><strong>Jebena</strong></td>
                        <td>Diaspora-focused</td>
                        <td>Email & phone validation</td>
                        <td>Subscription-based</td>
                        <td>High match rate among diaspora</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="cards-grid" style="margin-top: 3rem;">
            <div class="card">
                <h3><i class="fas fa-check-circle" style="color: var(--green);"></i> Gojo Success Factors</h3>
                <p>Successfully leveraged the "Blue Checkmark" concept to build a community of 400,000 users, indicating that visible signals of verification are powerful drivers of engagement.</p>
            </div>
            <div class="card">
                <h3><i class="fas fa-lightbulb" style="color: var(--gold);"></i> Maraki Innovation</h3>
                <p>Introduction of relationship counseling services addresses unique cultural nuance: high value placed on expert guidance and mental health in family building.</p>
            </div>
            <div class="card">
                <h3><i class="fas fa-user-shield" style="color: var(--accent);"></i> Ethio Marriage Approach</h3>
                <p>Banning real photos in favor of avatars promotes "personality-first" dating, addressing judgment-heavy swiping culture.</p>
            </div>
        </div>
    </section>

    <!-- Biometric Section -->
    <section id="biometric">
        <div class="section-header">
            <h2>Biometric Identity Architecture</h2>
            <p>Advanced verification systems optimized for diverse African skin tones</p>
        </div>

        <div class="cards-grid">
            <div class="card">
                <div class="card-icon"><i class="fas fa-camera"></i></div>
                <h3>Facial Recognition</h3>
                <p><strong>Smile ID Integration:</strong> 99.8% accuracy rate for African faces. Two-step process matching live capture against uploaded profile images and ID documents.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-fingerprint"></i></div>
                <h3>Liveness Detection</h3>
                <p>Passive and active checks to prevent spoofing. Active liveness requires head turns or blinking; passive uses ML to detect textures distinguishing real faces from photos.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-id-card"></i></div>
                <h3>Fayda National ID</h3>
                <p>Integration with Proclamation No. 1284/2023. eKYC APIs verify user's name, age, and identity in real-time via OAuth 2.0 and OpenID Connect protocols.</p>
            </div>
        </div>

        <div class="table-container" style="margin-top: 3rem;">
            <table>
                <thead>
                    <tr>
                        <th>Verification Component</th>
                        <th>Technical Solution</th>
                        <th>Benefit to Ecosystem</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Face Matching</strong></td>
                        <td>Smile ID / Sumsub SDK</td>
                        <td>Ensures profile photos match the user</td>
                    </tr>
                    <tr>
                        <td><strong>Liveness Check</strong></td>
                        <td>FacePlugin / 3DiVi</td>
                        <td>Prevents deepfakes and photo spoofing</td>
                    </tr>
                    <tr>
                        <td><strong>Legal ID Check</strong></td>
                        <td>Fayda eKYC API</td>
                        <td>Confirms user is a registered resident</td>
                    </tr>
                    <tr>
                        <td><strong>Age Verification</strong></td>
                        <td>Fayda Date of Birth</td>
                        <td>Enforces 18+ requirement legally</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Location Verification -->
    <section id="location" style="background: var(--secondary);">
        <div class="section-header">
            <h2>Network-Based Location Verification</h2>
            <p>Theft-free location confirmation via cellular network triangulation</p>
        </div>

        <div class="highlight-box">
            <strong><i class="fas fa-map-marker-alt"></i> Critical Requirement:</strong> 
            Standard device-level GPS is easily manipulated by "fake GPS" applications. 
            Location verification must exceed device capabilities through carrier-based validation.
        </div>

        <div class="cards-grid">
            <div class="card">
                <div class="card-icon"><i class="fas fa-broadcast-tower"></i></div>
                <h3>Cellular Triangulation</h3>
                <p>LBS APIs via GSMA Open Gateway initiative query network operators (Ethio Telecom, Safaricom) to determine if SIM-based device is within claimed geographical area.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-shield-virus"></i></div>
                <h3>Anti-Spoofing</h3>
                <p>Location is "theft-free" because it relies on cell tower communication rather than device OS data. Prevents fake GPS app manipulation.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-map-marked-alt"></i></div>
                <h3>Geofencing</h3>
                <p>Proximity verification for high-trust actions (sending gifts, requesting dates). Validates presence in specific neighborhoods like Bole or Kazanchis.</p>
            </div>
        </div>

        <div class="table-container" style="margin-top: 3rem;">
            <table>
                <thead>
                    <tr>
                        <th>Location Method</th>
                        <th>Source of Data</th>
                        <th>Spoofability</th>
                        <th>Accuracy</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Device GPS</strong></td>
                        <td>Satellite (OS level)</td>
                        <td style="color: var(--accent);">High (Mock location apps)</td>
                        <td>High (3-10m)</td>
                    </tr>
                    <tr>
                        <td><strong>WiFi Triangulation</strong></td>
                        <td>Nearby Hotspots</td>
                        <td style="color: var(--gold);">Medium (VPN/Proxy)</td>
                        <td>Medium (20-50m)</td>
                    </tr>
                    <tr>
                        <td><strong>Cell ID (LBS)</strong></td>
                        <td>Network Towers</td>
                        <td style="color: var(--green);">Low (SIM-based)</td>
                        <td>Low to Medium (500m-2km)</td>
                    </tr>
                    <tr>
                        <td><strong>IP Address</strong></td>
                        <td>ISP Node</td>
                        <td style="color: var(--accent);">High (VPN/Tor)</td>
                        <td>Low (City level)</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing">
        <div class="section-header">
            <h2>Subscription Economy</h2>
            <p>Flexible billing cycles for diverse income levels from diaspora to local students</p>
        </div>

        <div class="highlight-box">
            <strong><i class="fas fa-chart-line"></i> Market Benchmark:</strong> 
            Analysis of Sewasew music streaming indicates successful pricing at 21 ETB weekly and 90 ETB monthly. 
            Verified dating apps can adjust upward for premium tiers.
        </div>

        <div class="pricing-grid">
            <div class="pricing-card">
                <h3>Daily Access</h3>
                <div class="price">10 <span>ETB/day</span></div>
                <ul class="features">
                    <li><i class="fas fa-check"></i> 24-hour full access</li>
                    <li><i class="fas fa-check"></i> Basic matching</li>
                    <li><i class="fas fa-check"></i> Profile verification</li>
                    <li><i class="fas fa-check"></i> Limited messaging</li>
                </ul>
                <p style="color: var(--text-muted); font-size: 0.9rem;">Perfect for temporary boosts or impulse usage</p>
            </div>

            <div class="pricing-card featured">
                <h3>Weekly Plan</h3>
                <div class="price">50 <span>ETB/week</span></div>
                <ul class="features">
                    <li><i class="fas fa-check"></i> Unlimited matching</li>
                    <li><i class="fas fa-check"></i> Priority support</li>
                    <li><i class="fas fa-check"></i> Advanced filters</li>
                    <li><i class="fas fa-check"></i> Read receipts</li>
                    <li><i class="fas fa-check"></i> Profile boosts</li>
                </ul>
                <p style="color: var(--text-muted); font-size: 0.9rem;">Regular users testing the platform</p>
            </div>

            <div class="pricing-card">
                <h3>Monthly Premium</h3>
                <div class="price">180 <span>ETB/month</span></div>
                <ul class="features">
                    <li><i class="fas fa-check"></i> All Weekly features</li>
                    <li><i class="fas fa-check"></i> Incognito browsing</li>
                    <li><i class="fas fa-check"></i> See who liked you</li>
                    <li><i class="fas fa-check"></i> Video calling</li>
                    <li><i class="fas fa-check"></i> Relationship counseling</li>
                </ul>
                <p style="color: var(--text-muted); font-size: 0.9rem;">Serious seekers leading to marriage</p>
            </div>

            <div class="pricing-card" style="border-color: var(--gold);">
                <h3>Quarterly/Annual</h3>
                <div class="price">600+ <span>ETB</span></div>
                <ul class="features">
                    <li><i class="fas fa-check"></i> All Premium features</li>
                    <li><i class="fas fa-check"></i> VIP badge</li>
                    <li><i class="fas fa-check"></i> Personal matchmaker</li>
                    <li><i class="fas fa-check"></i> Event invitations</li>
                    <li><i class="fas fa-check"></i> Diaspora features</li>
                </ul>
                <p style="color: var(--text-muted); font-size: 0.9rem;">High-intent users and diaspora</p>
            </div>
        </div>

        <div class="cards-grid" style="margin-top: 3rem;">
            <div class="card">
                <h3><i class="fas fa-mobile-alt" style="color: var(--accent);"></i> Telebirr Integration</h3>
                <p><strong>Mandate Contract System:</strong> Scheduled deductions from mobile wallet without requiring PIN for every transaction. Uses Fabric Token authentication and DisburseOrder API.</p>
            </div>
            <div class="card">
                <h3><i class="fas fa-credit-card" style="color: var(--gold);"></i> Chapa Aggregation</h3>
                <p>Unified interface for Telebirr, CBE Birr, and international cards. Handles webhooks for immediate premium feature provisioning upon payment.</p>
            </div>
        </div>
    </section>

    <!-- Compliance Section -->
    <section id="compliance" style="background: var(--secondary);">
        <div class="section-header">
            <h2>Data Protection & Compliance</h2>
            <p>Adherence to PDPP No. 1321/2024 and Data Sovereignty requirements</p>
        </div>

        <div class="highlight-box" style="background: rgba(46, 204, 113, 0.1); border-left-color: var(--green);">
            <strong><i class="fas fa-gavel"></i> Legal Framework:</strong> 
            Personal Data Protection Proclamation (PDPP) No. 1321/2024 defines "Personal Data" broadly to include location data, 
            online identifiers, and biometric characteristics. Processing sensitive data requires explicit, informed consent.
        </div>

        <div class="compliance-grid">
            <div class="compliance-card">
                <h4><i class="fas fa-bullseye"></i> Purpose Limitation</h4>
                <p>Data collected for verification cannot be used for unrelated third-party marketing without additional consent.</p>
            </div>
            <div class="compliance-card">
                <h4><i class="fas fa-compress-alt"></i> Data Minimization</h4>
                <p>Only the minimum necessary data for verification and matchmaking should be collected and stored.</p>
            </div>
            <div class="compliance-card">
                <h4><i class="fas fa-edit"></i> Accuracy & Rectification</h4>
                <p>Users have the right to access their data and correct any mistakes, such as age or location information.</p>
            </div>
            <div class="compliance-card">
                <h4><i class="fas fa-trash-alt"></i> Right to Erasure</h4>
                <p>Users must be able to delete their account and have all associated personal data destroyed by controllers and processors.</p>
            </div>
            <div class="compliance-card">
                <h4><i class="fas fa-server"></i> Data Sovereignty</h4>
                <p>Personal data of Ethiopian citizens must ideally be stored within national borders using local cloud providers like Websprix or Wingu Africa.</p>
            </div>
            <div class="compliance-card">
                <h4><i class="fas fa-exclamation-circle"></i> Penalties</h4>
                <p>Severe violations carry penalties up to 500,000 Birr, emphasizing the need for robust cybersecurity measures.</p>
            </div>
        </div>
    </section>

    <!-- Cultural Engineering -->
    <section class="cultural-section">
        <div class="section-header">
            <h2>Cultural Engineering & Algorithms</h2>
            <p>Reflecting the unique cultural nuances of the Horn of Africa</p>
        </div>

        <div class="cultural-grid">
            <div class="cultural-card">
                <h3 style="color: var(--gold); margin-bottom: 1rem;"><i class="fas fa-pray"></i> Religion as Hard Filter</h3>
                <p>In Ethiopia, religion is often a "hard" filter. Ethiopian Orthodox, Muslim, and Protestant communities frequently seek partners exclusively within the same faith. The algorithm must allow users to set these as mandatory criteria.</p>
            </div>
            <div class="cultural-card">
                <h3 style="color: var(--gold); margin-bottom: 1rem;"><i class="fas fa-language"></i> Language Compatibility</h3>
                <p>With over 80 ethnic groups, linguistic similarity (Amharic, Oromiffa, Tigrinya) remains a primary driver of initial connection. Platform utilizes Fayda-linked onboarding data for cultural compatibility scoring.</p>
            </div>
            <div class="cultural-card">
                <h3 style="color: var(--gold); margin-bottom: 1rem;"><i class="fas fa-ring"></i> Marriage Pacing</h3>
                <p>Women often bring up marriage early in conversations—reflecting serious intent typical of local culture. "Intent Badges" and "Timeline Preferences" help align expectations and reduce time-wasting.</p>
            </div>
            <div class="cultural-card">
                <h3 style="color: var(--gold); margin-bottom: 1rem;"><i class="fas fa-heart"></i> Relationship Counseling</h3>
                <p>Offering 1-on-1 sessions with trained coaches in local languages elevates the platform from discovery tool to comprehensive relationship ecosystem.</p>
            </div>
        </div>

        <div class="table-container" style="margin-top: 3rem;">
            <table>
                <thead>
                    <tr>
                        <th>Cultural Variable</th>
                        <th>Algorithmic Treatment</th>
                        <th>Social Rationale</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Religion</strong></td>
                        <td>Hard Filter / High Weight</td>
                        <td>Religious endogamy is common in the church/mosque</td>
                    </tr>
                    <tr>
                        <td><strong>Language</strong></td>
                        <td>Preference / Matching Score</td>
                        <td>Shared language facilitates deep connection</td>
                    </tr>
                    <tr>
                        <td><strong>Ethnicity</strong></td>
                        <td>Optional Preference</td>
                        <td>Reflects regional customs and family ties</td>
                    </tr>
                    <tr>
                        <td><strong>Relationship Intent</strong></td>
                        <td>Intent-based Discovery</td>
                        <td>Distinguishes marriage-seekers from casual daters</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Implementation Roadmap -->
    <section id="roadmap" class="tech-specs">
        <div class="section-header">
            <h2>Technical Implementation Roadmap</h2>
            <p>Five-layer architecture for the Ethio-Connect platform</p>
        </div>

        <div class="roadmap">
            <div class="roadmap-item">
                <div class="roadmap-content">
                    <h4 style="color: var(--gold); margin-bottom: 0.5rem;">1. Identity Layer</h4>
                    <p>Integrate Smile ID SDK for biometric liveness and face matching. Apply for Fayda eKYC API access through NIDP to verify legal identity.</p>
                    <div class="code-block">
<span class="comment"># Smile ID Integration Example</span>
<span class="keyword">from</span> smile_id <span class="keyword">import</span> WebApi

<span class="function">verify_user</span>(selfie_image, id_photo):
    api = WebApi(<span class="string">"partner_id"</span>, <span class="string">"api_key"</span>)
    <span class="keyword">return</span> api.submit_job({
        <span class="string">"user_id"</span>: user_id,
        <span class="string">"job_type"</span>: <span class="string">"biometric_kyc"</span>,
        <span class="string">"images"</span>: [selfie_image, id_photo]
    })
                    </div>
                </div>
                <div class="roadmap-dot"></div>
            </div>

            <div class="roadmap-item">
                <div class="roadmap-content">
                    <h4 style="color: var(--gold); margin-bottom: 0.5rem;">2. Communication Layer</h4>
                    <p>Register Sender ID with ECA and integrate with local SMS gateway (Africala) for OTP authentication and notifications.</p>
                </div>
                <div class="roadmap-dot"></div>
            </div>

            <div class="roadmap-item">
                <div class="roadmap-content">
                    <h4 style="color: var(--gold); margin-bottom: 0.5rem;">3. Fintech Layer</h4>
                    <p>Implement Chapa for unified payments. Configure Telebirr Mandate Contract API for daily, weekly, and monthly recurring billing.</p>
                    <div class="code-block">
<span class="comment"># Telebirr Mandate Contract Flow</span>
<span class="keyword">def</span> <span class="function">create_subscription</span>(user_phone, plan):
    <span class="comment"># 1. Mandate Signing - Redirect to Telebirr SuperApp</span>
    <span class="comment"># 2. Fabric Token Application</span>
    <span class="comment"># 3. Mandate Query - Verify active agreement</span>
    <span class="comment"># 4. DisburseOrder API - Execute scheduled deduction</span>
    <span class="keyword">pass</span>
                    </div>
                </div>
                <div class="roadmap-dot"></div>
            </div>

            <div class="roadmap-item">
                <div class="roadmap-content">
                    <h4 style="color: var(--gold); margin-bottom: 0.5rem;">4. Location Layer</h4>
                    <p>Integrate with carrier LBS gateways via GSMA Open Gateway APIs to verify SIM-based location and prevent GPS spoofing.</p>
                </div>
                <div class="roadmap-dot"></div>
            </div>

            <div class="roadmap-item">
                <div class="roadmap-content">
                    <h4 style="color: var(--gold); margin-bottom: 0.5rem;">5. Hosting & Compliance</h4>
                    <p>Deploy on local cloud provider (Websprix/Wingu Africa) to ensure PDPP 1321/2024 data sovereignty compliance.</p>
                </div>
                <div class="roadmap-dot"></div>
            </div>
        </div>
    </section>

    <!-- Developer Prompt Section -->
    <section style="background: var(--primary);">
        <div class="section-header">
            <h2>Deep Developer Prompt</h2>
            <p>Technical specification for AI development assistance</p>
        </div>

        <div style="max-width: 1000px; margin: 0 auto; background: rgba(0,0,0,0.3); border-radius: 20px; padding: 2rem; border: 1px solid rgba(255,255,255,0.1);">
            <h3 style="color: var(--accent); margin-bottom: 1rem; font-family: 'Playfair Display', serif;">Strategic Project Prompt: "Ethio-Connect"</h3>
            <p style="margin-bottom: 1.5rem; color: var(--text-muted);">
                <em>"Assume the role of a Principal Software Architect specializing in African Fintech and Biometric Identity Systems..."</em>
            </p>
            
            <div style="display: grid; gap: 1rem;">
                <div style="padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 10px; border-left: 3px solid var(--accent);">
                    <strong style="color: var(--gold);">1. Verification & Identity:</strong>
                    <p style="margin-top: 0.5rem; font-size: 0.9rem;">Multi-factor flow using Smile ID Biometric KYC, Fayda eKYC API (VeriFayda 2.0), and liveness detection.</p>
                </div>
                <div style="padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 10px; border-left: 3px solid var(--accent);">
                    <strong style="color: var(--gold);">2. Network-Validated Geofencing:</strong>
                    <p style="margin-top: 0.5rem; font-size: 0.9rem;">Location Trust Score system using GSMA/Camara Location Verification API cross-referencing GPS with cell tower data.</p>
                </div>
                <div style="padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 10px; border-left: 3px solid var(--accent);">
                    <strong style="color: var(--gold);">3. Subscription & Billing:</strong>
                    <p style="margin-top: 0.5rem; font-size: 0.9rem;">Chapa SDK for payments, Telebirr Mandate Contract for recurring billing (Daily: 10 ETB, Weekly: 50 ETB, Monthly: 180 ETB).</p>
                </div>
                <div style="padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 10px; border-left: 3px solid var(--accent);">
                    <strong style="color: var(--gold);">4. Data Sovereignty:</strong>
                    <p style="margin-top: 0.5rem; font-size: 0.9rem;">PDPP No. 1321/2024 compliance with AES-256 encryption, local cloud hosting, and Global Delete functionality.</p>
                </div>
                <div style="padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 10px; border-left: 3px solid var(--accent);">
                    <strong style="color: var(--gold);">5. Cultural Algorithm:</strong>
                    <p style="margin-top: 0.5rem; font-size: 0.9rem;">Weighting system with Religion as mandatory hard-filter, Language and Intent as high-priority factors.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Conclusion -->
    <section style="background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);">
        <div class="section-header">
            <h2>Synthesis & Future Outlook</h2>
            <p>The social mission to rebuild trust in the digital sphere</p>
        </div>

        <div style="max-width: 900px; margin: 0 auto; text-align: center;">
            <p style="font-size: 1.2rem; line-height: 1.8; margin-bottom: 2rem;">
                The development of a dating application for the Ethiopian community is not merely a technical endeavor but a 
                <span style="color: var(--accent); font-weight: 600;">social mission to rebuild trust in the digital sphere</span>. 
                By strictly enforcing biometric and network-based verification, the platform directly addresses the primary grievances 
                of the local user base: the fear of fraud and deception.
            </p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <div style="padding: 2rem; background: var(--glass); border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);">
                    <i class="fas fa-id-card" style="font-size: 2rem; color: var(--gold); margin-bottom: 1rem;"></i>
                    <h4 style="margin-bottom: 0.5rem;">2028 Target</h4>
                    <p style="color: var(--text-muted);">90 million Fayda National ID registrations creating pool of pre-verified citizens</p>
                </div>
                <div style="padding: 2rem; background: var(--glass); border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);">
                    <i class="fas fa-mobile-alt" style="font-size: 2rem; color: var(--gold); margin-bottom: 1rem;"></i>
                    <h4 style="margin-bottom: 0.5rem;">M-Pesa Integration</h4>
                    <p style="color: var(--text-muted);">Safaricom M-Pesa inclusion expanding recurring billing reach</p>
                </div>
                <div style="padding: 2rem; background: var(--glass); border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);">
                    <i class="fas fa-heart" style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem;"></i>
                    <h4 style="margin-bottom: 0.5rem;">E-Habesha Ecosystem</h4>
                    <p style="color: var(--text-muted);">Safe, professional, culturally resonant space for building families</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h4>Research Areas</h4>
                <ul>
                    <li><a href="#biometric">Biometric Verification</a></li>
                    <li><a href="#location">Location Services</a></li>
                    <li><a href="#pricing">Fintech Integration</a></li>
                    <li><a href="#compliance">Data Protection</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Technologies</h4>
                <ul>
                    <li><a href="#">Smile ID SDK</a></li>
                    <li><a href="#">Fayda eKYC API</a></li>
                    <li><a href="#">Telebirr Mandate</a></li>
                    <li><a href="#">Chapa Payments</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Legal Framework</h4>
                <ul>
                    <li><a href="#">PDPP No. 1321/2024</a></li>
                    <li><a href="#">Proclamation No. 1284/2023</a></li>
                    <li><a href="#">Computer Crime Proclamation 958/2016</a></li>
                    <li><a href="#">Data Sovereignty Requirements</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Connect</h4>
                <ul>
                    <li><a href="#"><i class="fas fa-envelope"></i> research@ethio-connect.et</a></li>
                    <li><a href="#"><i class="fas fa-globe"></i> ethio-connect.et</a></li>
                    <li><a href="#"><i class="fab fa-github"></i> Technical Documentation</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Ethio-Connect Research. All rights reserved. | Original Research Document</p>
        </div>
    </footer>

    <script>
        // Smooth scroll for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Navbar background on scroll
        window.addEventListener('scroll', () => {
            const nav = document.querySelector('nav');
            if (window.scrollY > 50) {
                nav.style.background = 'rgba(26, 26, 46, 0.98)';
            } else {
                nav.style.background = 'rgba(26, 26, 46, 0.9)';
            }
        });

        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe cards and sections
        document.querySelectorAll('.card, .pricing-card, .compliance-card, .cultural-card').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });

        // Counter animation for stats
        const animateCounter = (el) => {
            const target = el.innerText;
            const num = parseInt(target.replace(/[^0-9]/g, ''));
            const suffix = target.replace(/[0-9]/g, '');
            let current = 0;
            const increment = num / 50;
            const timer = setInterval(() => {
                current += increment;
                if (current >= num) {
                    el.innerText = target;
                    clearInterval(timer);
                } else {
                    el.innerText = Math.floor(current) + suffix;
                }
            }, 30);
        };

        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target.querySelector('.stat-number'));
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        document.querySelectorAll('.stat-item').forEach(stat => {
            statsObserver.observe(stat);
        });
    </script>
</body>
</html>
