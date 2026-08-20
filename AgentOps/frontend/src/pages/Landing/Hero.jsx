import { Link } from 'react-router-dom'
import { ArrowRight, Sparkles } from 'lucide-react'

function Hero() {
  return (
    <section className="pt-32 pb-20 px-6">

      <div className="max-w-7xl mx-auto">

        <div className="max-w-4xl mx-auto text-center">

          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-indigo-500/30 bg-indigo-500/10 text-indigo-300 text-sm mb-8">
            <Sparkles size={16} />
            AI-powered DSA learning
          </div>

          {/* Heading */}
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight leading-tight">

            Master DSA with your

            <span className="text-indigo-500">
              {' '}AI Coach
            </span>

          </h1>

          {/* Description */}
          <p className="mt-6 text-lg md:text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
            Learn data structures and algorithms through
            guided problem solving, intelligent hints,
            code analysis, and personalized feedback.
          </p>

          {/* Buttons */}
          <div className="mt-10 flex flex-col sm:flex-row justify-center gap-4">

            <Link
              to="/signup"
              className="flex items-center justify-center gap-2 px-6 py-3 rounded-lg bg-indigo-600 hover:bg-indigo-500 transition font-semibold"
            >
              Start Learning
              <ArrowRight size={18} />
            </Link>

            <Link
              to="/login"
              className="px-6 py-3 rounded-lg border border-white/10 hover:bg-white/5 transition font-semibold"
            >
              Explore DSA Coach
            </Link>

          </div>

        </div>

        {/* Editor Preview */}
        <div className="mt-20 max-w-5xl mx-auto">

          <div className="rounded-xl border border-white/10 bg-slate-900 shadow-2xl overflow-hidden">

            {/* Editor Header */}
            <div className="h-11 border-b border-white/10 flex items-center px-4 gap-2">

              <div className="w-3 h-3 rounded-full bg-red-400" />
              <div className="w-3 h-3 rounded-full bg-yellow-400" />
              <div className="w-3 h-3 rounded-full bg-green-400" />

              <span className="ml-4 text-sm text-slate-500">
                solution.java
              </span>

            </div>

            {/* Code */}
            <div className="p-6 text-left font-mono text-sm overflow-x-auto">

              <div>
                <span className="text-purple-400">class</span>{' '}
                <span className="text-blue-400">Solution</span>{' '}
                {'{'}
              </div>

              <div className="pl-6">
                <span className="text-purple-400">public</span>{' '}
                <span className="text-purple-400">int</span>{' '}
                twoSum(int[] nums, int target) {'{'}
              </div>

              <div className="pl-12 text-slate-400">
                // Your solution goes here
              </div>

              <div className="pl-6">
                {'}'}
              </div>

              <div>
                {'}'}
              </div>

            </div>

          </div>

        </div>

      </div>

    </section>
  )
}

export default Hero