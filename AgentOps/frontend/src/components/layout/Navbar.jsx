import { Link } from 'react-router-dom'
import { Code2, Menu, X } from 'lucide-react'
import { useState } from 'react'

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 border-b border-white/10 bg-slate-950/90 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

        {/* Logo */}
        <Link
          to="/"
          className="flex items-center gap-2"
        >
          <div className="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center">
            <Code2 size={22} />
          </div>

          <span className="text-xl font-bold">
            DSA Coach
          </span>
        </Link>

        {/* Desktop Navigation */}
        <div className="hidden md:flex items-center gap-8">

          <a href="#features" className="text-slate-300 hover:text-white transition">
            Features
          </a>

          <a href="#ai-coach" className="text-slate-300 hover:text-white transition">
            AI Coach
          </a>

          <a href="#coding" className="text-slate-300 hover:text-white transition">
            Coding
          </a>

        </div>

        {/* Desktop Buttons */}
        <div className="hidden md:flex items-center gap-3">

          <Link
            to="/login"
            className="px-4 py-2 text-slate-300 hover:text-white transition"
          >
            Login
          </Link>

          <Link
            to="/signup"
            className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 transition font-medium"
          >
            Get Started
          </Link>

        </div>

        {/* Mobile Menu Button */}
        <button
          onClick={() => setMenuOpen(!menuOpen)}
          className="md:hidden text-slate-300"
        >
          {menuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>

      </div>

      {/* Mobile Menu */}
      {menuOpen && (
        <div className="md:hidden border-t border-white/10 bg-slate-950 px-6 py-5">

          <div className="flex flex-col gap-5">

            <a
              href="#features"
              onClick={() => setMenuOpen(false)}
              className="text-slate-300"
            >
              Features
            </a>

            <a
              href="#ai-coach"
              onClick={() => setMenuOpen(false)}
              className="text-slate-300"
            >
              AI Coach
            </a>

            <a
              href="#coding"
              onClick={() => setMenuOpen(false)}
              className="text-slate-300"
            >
              Coding
            </a>

            <Link
              to="/login"
              className="text-slate-300"
            >
              Login
            </Link>

            <Link
              to="/signup"
              className="bg-indigo-600 px-4 py-2 rounded-lg text-center"
            >
              Get Started
            </Link>

          </div>

        </div>
      )}
    </nav>
  )
}

export default Navbar