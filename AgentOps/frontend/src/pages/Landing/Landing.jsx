import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Brain,
  Code2,
  Sparkles,
  ChevronRight,
  Terminal,
  CheckCircle2,
  Zap,
  BarChart3,
  MessageSquareCode,
  Lightbulb,
  Layers,
  Cpu,
  ArrowRight,
  Star,
  Menu,
  X,
  Target,
  FileCode2,
  Bot
} from 'lucide-react';

export default function LandingPage() {
  const navigate = useNavigate();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleGetStarted = () => {
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-[#F8FAFC] text-[#0F172A] font-sans antialiased selection:bg-blue-100 selection:text-blue-700">
      
      {/* ================= 1. GLOBAL FLOATING PILL HEADER ================= */}
      <header className="sticky top-6 z-50 max-w-5xl mx-auto px-4">
        <nav className="bg-white/80 backdrop-blur-md border border-[#E2E8F0] shadow-sm rounded-full px-6 py-3 flex items-center justify-between transition-all">
          {/* Logo */}
          <div 
            className="flex items-center gap-2.5 cursor-pointer group"
            onClick={() => navigate('/')}
          >
            <div className="w-9 h-9 rounded-full bg-[#2563EB] flex items-center justify-center text-white shadow-sm group-hover:scale-105 transition-transform">
              <Brain className="w-5 h-5" />
            </div>
            <span className="font-bold text-lg text-[#0F172A] tracking-tight">
              DSA Coach <span className="text-[#2563EB] text-xs font-semibold px-2 py-0.5 bg-blue-50 rounded-full border border-blue-100 ml-1">AI</span>
            </span>
          </div>

          {/* Center Navigation Links */}
          <div className="hidden md:flex items-center gap-8 text-sm font-medium text-[#64748B]">
            <a href="#home" className="hover:text-[#2563EB] transition-colors">Home</a>
            <a href="#features" className="hover:text-[#2563EB] transition-colors">Features</a>
            <a href="#how-it-works" className="hover:text-[#2563EB] transition-colors">How It Works</a>
            <a href="#about" className="hover:text-[#2563EB] transition-colors">About Us</a>
            <a href="#testimonials" className="hover:text-[#2563EB] transition-colors">Testimonials</a>
          </div>

          {/* Right Action Button */}
          <div className="hidden md:flex items-center">
            <button
              onClick={handleGetStarted}
              className="bg-[#2563EB] hover:bg-blue-700 text-white font-medium text-sm px-5 py-2 rounded-full shadow-sm hover:shadow transition-all flex items-center gap-1.5 active:scale-95"
            >
              Get Started
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>

          {/* Mobile Hamburger Toggle */}
          <div className="md:hidden flex items-center gap-2">
            <button
              onClick={handleGetStarted}
              className="bg-[#2563EB] text-white text-xs font-medium px-3.5 py-1.5 rounded-full"
            >
              Get Started
            </button>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-1.5 text-[#64748B] hover:text-[#0F172A] focus:outline-none"
              aria-label="Toggle menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </nav>

        {/* Mobile Menu Overlay */}
        {mobileMenuOpen && (
          <div className="md:hidden mt-3 bg-white border border-[#E2E8F0] rounded-2xl p-5 shadow-lg flex flex-col gap-4 text-sm font-medium text-[#64748B]">
            <a href="#home" onClick={() => setMobileMenuOpen(false)} className="hover:text-[#2563EB]">Home</a>
            <a href="#features" onClick={() => setMobileMenuOpen(false)} className="hover:text-[#2563EB]">Features</a>
            <a href="#how-it-works" onClick={() => setMobileMenuOpen(false)} className="hover:text-[#2563EB]">How It Works</a>
            <a href="#about" onClick={() => setMobileMenuOpen(false)} className="hover:text-[#2563EB]">About Us</a>
            <a href="#testimonials" onClick={() => setMobileMenuOpen(false)} className="hover:text-[#2563EB]">Testimonials</a>
          </div>
        )}
      </header>


      {/* ================= 2. HERO SECTION ================= */}
      <section id="home" className="pt-20 pb-16 px-4 max-w-6xl mx-auto text-center">
        {/* Pill Badge */}
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-100 text-[#2563EB] text-xs font-semibold mb-6 shadow-sm">
          <Sparkles className="w-3.5 h-3.5 text-[#2563EB]" />
          <span>Next-Generation Technical Interview Platform</span>
        </div>

        {/* Main Heading */}
        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-[#0F172A] tracking-tight leading-[1.15] max-w-4xl mx-auto">
          Your AI-Powered <span className="text-[#2563EB]">DSA Mentor</span>
        </h1>

        {/* Supporting Copy */}
        <p className="mt-6 text-lg sm:text-xl text-[#64748B] max-w-2xl mx-auto font-normal leading-relaxed">
          Learn Data Structures and Algorithms, solve complex problems, debug your code, and prepare for technical interviews with an AI mentor that guides you step by step.
        </p>

        {/* CTAs */}
        <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
          <button
            onClick={handleGetStarted}
            className="w-full sm:w-auto bg-[#2563EB] hover:bg-blue-700 text-white font-semibold text-base px-7 py-3.5 rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2 active:scale-98"
          >
            Get Started Free
            <ArrowRight className="w-5 h-5" />
          </button>
          <a
            href="#features"
            className="w-full sm:w-auto bg-white hover:bg-slate-100 text-[#0F172A] font-semibold text-base px-7 py-3.5 rounded-xl border border-[#E2E8F0] shadow-sm transition-all text-center"
          >
            Explore DSA Coach
          </a>
        </div>

        {/* Hero Visual Showcase */}
        <div className="mt-14 relative max-w-5xl mx-auto rounded-2xl border border-[#E2E8F0] bg-white p-3 shadow-xl overflow-hidden">
          <div className="bg-[#0F172A] rounded-xl p-4 sm:p-6 text-left text-white font-mono text-xs sm:text-sm overflow-x-auto relative">
            
            {/* Top Editor Bar */}
            <div className="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                <span className="w-3 h-3 rounded-full bg-yellow-500 inline-block"></span>
                <span className="w-3 h-3 rounded-full bg-green-500 inline-block"></span>
                <span className="text-slate-400 font-sans text-xs ml-2 flex items-center gap-1.5">
                  <FileCode2 className="w-3.5 h-3.5 text-blue-400" />
                  two_sum_solution.py
                </span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs bg-blue-500/20 text-blue-300 border border-blue-500/30 px-2.5 py-0.5 rounded-full flex items-center gap-1 font-sans">
                  <Bot className="w-3 h-3" /> AI Feedback Active
                </span>
              </div>
            </div>

            {/* Code & Visual Split */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
              {/* Code Snippet */}
              <div className="lg:col-span-7 space-y-1 text-slate-300">
                <p><span className="text-purple-400">def</span> <span className="text-blue-400">twoSum</span>(nums, target):</p>
                <p className="pl-4 text-slate-500"># Hash map for O(n) lookup time</p>
                <p className="pl-4">seen = {}</p>
                <p className="pl-4"><span className="text-purple-400">for</span> i, num <span className="text-purple-400">in</span> <span className="text-blue-400">enumerate</span>(nums):</p>
                <p className="pl-8">complement = target - num</p>
                <p className="pl-8"><span className="text-purple-400">if</span> complement <span className="text-purple-400">in</span> seen:</p>
                <p className="pl-12 text-green-400"><span className="text-purple-400">return</span> [seen[complement], i]</p>
                <p className="pl-8">seen[num] = i</p>
              </div>

              {/* AI Guidance Overlay */}
              <div className="lg:col-span-5 bg-slate-800/90 rounded-lg p-4 border border-slate-700/80 font-sans text-xs text-slate-200">
                <div className="flex items-center gap-2 text-blue-400 font-semibold mb-2">
                  <Sparkles className="w-4 h-4 text-blue-400" />
                  AI Mentor Hint #1
                </div>
                <p className="text-slate-300 leading-relaxed">
                  Excellent approach! You optimized the time complexity from <code className="bg-slate-900 px-1 py-0.5 rounded text-amber-300">O(N²)</code> to <code className="bg-slate-900 px-1 py-0.5 rounded text-green-300">O(N)</code> using a Hash Table.
                </p>
                <div className="mt-3 pt-3 border-t border-slate-700/60 flex items-center justify-between text-[11px] text-slate-400">
                  <span>Time Complexity: <strong className="text-green-400">O(N)</strong></span>
                  <span>Space Complexity: <strong className="text-amber-400">O(N)</strong></span>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>


      {/* ================= 3. TRUST / TECHNOLOGY STRIP ================= */}
      <section className="py-8 border-y border-[#E2E8F0] bg-white">
        <div className="max-w-6xl mx-auto px-4">
          <p className="text-center text-xs font-semibold text-[#64748B] uppercase tracking-wider mb-6">
            Powered By Cutting-Edge Developer Technology
          </p>
          <div className="flex flex-wrap items-center justify-center gap-6 sm:gap-10 text-sm font-medium text-[#0F172A]">
            <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0]">
              <Cpu className="w-4 h-4 text-[#2563EB]" />
              <span>AI-Powered Mentorship</span>
            </div>
            <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0]">
              <Layers className="w-4 h-4 text-[#2563EB]" />
              <span>RAG Knowledge Base</span>
            </div>
            <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0]">
              <Code2 className="w-4 h-4 text-[#2563EB]" />
              <span>Structured DSA Practice</span>
            </div>
            <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0]">
              <Terminal className="w-4 h-4 text-[#2563EB]" />
              <span>Code & Complexity Analysis</span>
            </div>
            <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0]">
              <Target className="w-4 h-4 text-[#2563EB]" />
              <span>Interview Prep Sheets</span>
            </div>
          </div>
        </div>
      </section>


      {/* ================= 4. FEATURES SECTION ================= */}
      <section id="features" className="py-20 px-4 max-w-6xl mx-auto">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-3xl sm:text-4xl font-extrabold text-[#0F172A] tracking-tight">
            Everything You Need to Master DSA
          </h2>
          <p className="mt-4 text-base sm:text-lg text-[#64748B]">
            Stop getting stuck on leetcode problems for hours. Get tailored guidance, intelligent hint progression, and targeted interview prep.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {/* Card 1 */}
          <div className="bg-white rounded-2xl p-7 border border-[#E2E8F0] shadow-sm hover:shadow-md transition-shadow group flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <Brain className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-[#0F172A] mb-2">AI DSA Coach</h3>
              <p className="text-sm text-[#64748B] leading-relaxed">
                Ask questions, clarify concepts, and receive step-by-step personalized DSA guidance tailored to your learning pace.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center text-xs font-semibold text-[#2563EB]">
              <span>Ask & Contextualize</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </div>
          </div>

          {/* Card 2 */}
          <div className="bg-white rounded-2xl p-7 border border-[#E2E8F0] shadow-sm hover:shadow-md transition-shadow group flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <Lightbulb className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-[#0F172A] mb-2">Smart Hints</h3>
              <p className="text-sm text-[#64748B] leading-relaxed">
                Get progressive hints instead of immediately spoiling the full solution. Learn how to think, not just what to copy.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center text-xs font-semibold text-[#2563EB]">
              <span>Guided Problem Solving</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </div>
          </div>

          {/* Card 3 */}
          <div className="bg-white rounded-2xl p-7 border border-[#E2E8F0] shadow-sm hover:shadow-md transition-shadow group flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <MessageSquareCode className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-[#0F172A] mb-2">Code Analysis</h3>
              <p className="text-sm text-[#64748B] leading-relaxed">
                Understand why your code fails edge cases, audit Time & Space complexity, and fix bugs with instant automated code reviews.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center text-xs font-semibold text-[#2563EB]">
              <span>Real-time Feedback</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </div>
          </div>

          {/* Card 4 */}
          <div className="bg-white rounded-2xl p-7 border border-[#E2E8F0] shadow-sm hover:shadow-md transition-shadow group flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <Layers className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-[#0F172A] mb-2">Structured Practice</h3>
              <p className="text-sm text-[#64748B] leading-relaxed">
                Master problems organized by topic (Arrays, Graphs, DP, Trees) and difficulty with curated sheets like A2Z Sheet.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center text-xs font-semibold text-[#2563EB]">
              <span>Curated Problem Sets</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </div>
          </div>

          {/* Card 5 */}
          <div className="bg-white rounded-2xl p-7 border border-[#E2E8F0] shadow-sm hover:shadow-md transition-shadow group flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <Zap className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-[#0F172A] mb-2">Interview Preparation</h3>
              <p className="text-sm text-[#64748B] leading-relaxed">
                Simulate technical interviews with targeted questions, timed practice, and mock feedback for top tech companies.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center text-xs font-semibold text-[#2563EB]">
              <span>FAANG Ready</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </div>
          </div>

          {/* Card 6 */}
          <div className="bg-white rounded-2xl p-7 border border-[#E2E8F0] shadow-sm hover:shadow-md transition-shadow group flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                <BarChart3 className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-[#0F172A] mb-2">Progress Tracking</h3>
              <p className="text-sm text-[#64748B] leading-relaxed">
                Track your strengths, identify weak algorithm categories, and monitor your consistency with actionable dashboard metrics.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center text-xs font-semibold text-[#2563EB]">
              <span>Detailed Analytics</span>
              <ChevronRight className="w-4 h-4 ml-1" />
            </div>
          </div>
        </div>
      </section>


      {/* ================= 5. HOW IT WORKS SECTION ================= */}
      <section id="how-it-works" className="py-20 px-4 bg-white border-y border-[#E2E8F0]">
        <div className="max-w-6xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <h2 className="text-3xl sm:text-4xl font-extrabold text-[#0F172A] tracking-tight">
              How DSA Coach Works
            </h2>
            <p className="mt-4 text-base sm:text-lg text-[#64748B]">
              A proven 4-step workflow to help you build intuition and solve problems independently.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 relative">
            {/* Step 1 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-6 border border-[#E2E8F0] relative flex flex-col items-center text-center">
              <div className="w-10 h-10 rounded-full bg-[#2563EB] text-white font-bold text-sm flex items-center justify-center mb-4 shadow-sm">
                01
              </div>
              <h3 className="text-lg font-bold text-[#0F172A] mb-2">Choose a Problem</h3>
              <p className="text-xs text-[#64748B] leading-relaxed">
                Select from top interview sheets or topic-wise problems (Arrays, Graphs, DP).
              </p>
            </div>

            {/* Step 2 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-6 border border-[#E2E8F0] relative flex flex-col items-center text-center">
              <div className="w-10 h-10 rounded-full bg-[#2563EB] text-white font-bold text-sm flex items-center justify-center mb-4 shadow-sm">
                02
              </div>
              <h3 className="text-lg font-bold text-[#0F172A] mb-2">Understand Approach</h3>
              <p className="text-xs text-[#64748B] leading-relaxed">
                Request progressive hints or algorithm intuition without giving away full code.
              </p>
            </div>

            {/* Step 3 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-6 border border-[#E2E8F0] relative flex flex-col items-center text-center">
              <div className="w-10 h-10 rounded-full bg-[#2563EB] text-white font-bold text-sm flex items-center justify-center mb-4 shadow-sm">
                03
              </div>
              <h3 className="text-lg font-bold text-[#0F172A] mb-2">Write Your Solution</h3>
              <p className="text-xs text-[#64748B] leading-relaxed">
                Implement code inside the integrated Monaco code editor in your preferred language.
              </p>
            </div>

            {/* Step 4 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-6 border border-[#E2E8F0] relative flex flex-col items-center text-center">
              <div className="w-10 h-10 rounded-full bg-[#2563EB] text-white font-bold text-sm flex items-center justify-center mb-4 shadow-sm">
                04
              </div>
              <h3 className="text-lg font-bold text-[#0F172A] mb-2">Get AI Feedback</h3>
              <p className="text-xs text-[#64748B] leading-relaxed">
                Run tests, get complexity breakdowns, review edge cases, and refine your code.
              </p>
            </div>
          </div>
        </div>
      </section>


      {/* ================= 6. ABOUT US / WHY DSA COACH ================= */}
      <section id="about" className="py-20 px-4 max-w-6xl mx-auto">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div className="lg:col-span-6 space-y-6">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 text-[#2563EB] text-xs font-semibold border border-blue-100">
              Why DSA Coach AI?
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-[#0F172A] tracking-tight leading-tight">
              Designed for Engineers Who Want True Algorithm Intuition
            </h2>
            <p className="text-[#64748B] text-base leading-relaxed">
              Traditional coding platforms give you static test cases and immediate solution unlocks. DSA Coach acts as an active technical interviewer—offering guided hints, analyzing space-time tradeoffs, and teaching you the logic behind algorithms.
            </p>

            <div className="space-y-3 pt-2">
              <div className="flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-[#2563EB] shrink-0 mt-0.5" />
                <span className="text-sm text-[#0F172A] font-medium">Progressive hints prevent solution-spoilers</span>
              </div>
              <div className="flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-[#2563EB] shrink-0 mt-0.5" />
                <span className="text-sm text-[#0F172A] font-medium">Instant Time & Space complexity analysis</span>
              </div>
              <div className="flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-[#2563EB] shrink-0 mt-0.5" />
                <span className="text-sm text-[#0F172A] font-medium">Structured roadmap covering Striver's A2Z and top sheets</span>
              </div>
            </div>

            <div className="pt-4">
              <button
                onClick={handleGetStarted}
                className="bg-[#2563EB] hover:bg-blue-700 text-white font-semibold text-sm px-6 py-3 rounded-xl shadow transition-all inline-flex items-center gap-2"
              >
                Start Mentorship Now
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Image Mockup */}
          <div className="lg:col-span-6">
            <div className="relative rounded-2xl border border-[#E2E8F0] bg-white p-3 shadow-lg">
              <img
                src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1000&q=80"
                alt="Software Engineer Coding"
                className="rounded-xl w-full h-80 object-cover"
              />
              <div className="absolute -bottom-5 -left-5 bg-white p-4 rounded-xl border border-[#E2E8F0] shadow-lg hidden sm:flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-green-50 text-green-600 flex items-center justify-center font-bold">
                  98%
                </div>
                <div>
                  <p className="text-xs font-bold text-[#0F172A]">Problem Solved</p>
                  <p className="text-[11px] text-[#64748B]">Optimal Space-Time Complexity</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>


      {/* ================= 7. TESTIMONIALS SECTION ================= */}
      <section id="testimonials" className="py-20 px-4 bg-white border-t border-[#E2E8F0]">
        <div className="max-w-6xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <h2 className="text-3xl sm:text-4xl font-extrabold text-[#0F172A] tracking-tight">
              Trusted by Developers Worldwide
            </h2>
            <p className="mt-4 text-base sm:text-lg text-[#64748B]">
              Here is how DSA Coach helped candidate engineers prepare for top tech companies.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Testimonial 1 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-7 border border-[#E2E8F0] flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-1 text-amber-400 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 fill-amber-400" />
                  ))}
                </div>
                <p className="text-sm text-[#0F172A] leading-relaxed italic">
                  "The progressive hint system changed everything for me. Instead of peeking at solutions on LeetCode, DSA Coach forced me to think through graph traversals step by step."
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-slate-200 flex items-center gap-3">
                <img
                  src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80"
                  alt="User avatar"
                  className="w-10 h-10 rounded-full object-cover"
                />
                <div>
                  <p className="text-xs font-bold text-[#0F172A]">Sarah Chen</p>
                  <p className="text-[11px] text-[#64748B]">Software Engineer at Google</p>
                </div>
              </div>
            </div>

            {/* Testimonial 2 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-7 border border-[#E2E8F0] flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-1 text-amber-400 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 fill-amber-400" />
                  ))}
                </div>
                <p className="text-sm text-[#0F172A] leading-relaxed italic">
                  "Code analysis is spot on. It pinpointed an edge case in my Dynamic Programming memoization table in seconds. Highly recommended for interview prep."
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-slate-200 flex items-center gap-3">
                <img
                  src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80"
                  alt="User avatar"
                  className="w-10 h-10 rounded-full object-cover"
                />
                <div>
                  <p className="text-xs font-bold text-[#0F172A]">Alex Rivera</p>
                  <p className="text-[11px] text-[#64748B]">Frontend Engineer at Meta</p>
                </div>
              </div>
            </div>

            {/* Testimonial 3 */}
            <div className="bg-[#F8FAFC] rounded-2xl p-7 border border-[#E2E8F0] flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-1 text-amber-400 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 fill-amber-400" />
                  ))}
                </div>
                <p className="text-sm text-[#0F172A] leading-relaxed italic">
                  "Having an AI mentor embedded directly alongside the code editor made practicing A2Z sheet problems twice as fast and much less frustrating."
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-slate-200 flex items-center gap-3">
                <img
                  src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80"
                  alt="User avatar"
                  className="w-10 h-10 rounded-full object-cover"
                />
                <div>
                  <p className="text-xs font-bold text-[#0F172A]">David Kapoor</p>
                  <p className="text-[11px] text-[#64748B]">Backend Engineer at Amazon</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>


      {/* ================= 8. CALL TO ACTION (CTA) ================= */}
      <section className="py-20 px-4 max-w-5xl mx-auto">
        <div className="bg-[#0F172A] rounded-3xl p-8 sm:p-12 text-center text-white relative overflow-hidden shadow-2xl">
          <div className="relative z-10 max-w-2xl mx-auto">
            <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight">
              Ready to Master DSA & Land Your Dream Job?
            </h2>
            <p className="mt-4 text-slate-300 text-base sm:text-lg">
              Start practicing with your AI mentor today. Free to get started, no credit card required.
            </p>
            <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
              <button
                onClick={handleGetStarted}
                className="w-full sm:w-auto bg-[#2563EB] hover:bg-blue-600 text-white font-semibold text-base px-8 py-3.5 rounded-xl shadow-lg hover:shadow-blue-500/20 transition-all flex items-center justify-center gap-2"
              >
                Get Started Now
                <ArrowRight className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </section>


      {/* ================= 9. FOOTER ================= */}
      <footer className="bg-white border-t border-[#E2E8F0] py-12 px-4 text-sm text-[#64748B]">
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
          
          {/* Brand Info */}
          <div className="space-y-4 md:col-span-1">
            <div className="flex items-center gap-2">
              <div className="w-7 h-7 rounded-full bg-[#2563EB] flex items-center justify-center text-white">
                <Brain className="w-4 h-4" />
              </div>
              <span className="font-bold text-base text-[#0F172A]">DSA Coach AI</span>
            </div>
            <p className="text-xs text-[#64748B] leading-relaxed">
              Your AI mentor for Data Structures, Algorithms, and Technical Interview Prep.
            </p>
          </div>

          {/* Links Column 1 */}
          <div>
            <h4 className="font-semibold text-[#0F172A] mb-3 text-xs uppercase tracking-wider">Product</h4>
            <ul className="space-y-2 text-xs">
              <li><a href="#features" className="hover:text-[#2563EB]">Features</a></li>
              <li><a href="#how-it-works" className="hover:text-[#2563EB]">How It Works</a></li>
              <li><a href="#about" className="hover:text-[#2563EB]">About Us</a></li>
              <li><a href="#testimonials" className="hover:text-[#2563EB]">Testimonials</a></li>
            </ul>
          </div>

          {/* Links Column 2 */}
          <div>
            <h4 className="font-semibold text-[#0F172A] mb-3 text-xs uppercase tracking-wider">Practice</h4>
            <ul className="space-y-2 text-xs">
              <li><a href="/login" className="hover:text-[#2563EB]">A2Z Sheet</a></li>
              <li><a href="/login" className="hover:text-[#2563EB]">Practice Problems</a></li>
              <li><a href="/login" className="hover:text-[#2563EB]">Mock Interview Prep</a></li>
              <li><a href="/login" className="hover:text-[#2563EB]">MCQ Tests</a></li>
            </ul>
          </div>

          {/* Links Column 3 */}
          <div>
            <h4 className="font-semibold text-[#0F172A] mb-3 text-xs uppercase tracking-wider">Account</h4>
            <ul className="space-y-2 text-xs">
              <li><a href="/login" className="hover:text-[#2563EB]">Login</a></li>
              <li><a href="/login" className="hover:text-[#2563EB]">Sign Up</a></li>
              <li><a href="#" className="hover:text-[#2563EB]">Privacy Policy</a></li>
              <li><a href="#" className="hover:text-[#2563EB]">Terms of Service</a></li>
            </ul>
          </div>

        </div>

        <div className="max-w-6xl mx-auto mt-12 pt-6 border-t border-[#E2E8F0] flex flex-col sm:flex-row items-center justify-between text-xs text-[#64748B]">
          <p>© {new Date().getFullYear()} DSA Coach AI. All rights reserved.</p>
          <p className="mt-2 sm:mt-0">Built by AgentOps</p>
        </div>
      </footer>

    </div>
  );
} 