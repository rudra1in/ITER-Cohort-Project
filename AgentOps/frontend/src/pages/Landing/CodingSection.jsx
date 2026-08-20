import { Terminal, Play, Bug } from 'lucide-react'

function CodingSection() {
  return (
    <section
      id="coding"
      className="py-24 px-6"
    >

      <div className="max-w-7xl mx-auto">

        <div className="grid lg:grid-cols-2 gap-14 items-center">

          {/* Editor */}
          <div className="rounded-xl border border-white/10 bg-slate-900 overflow-hidden order-2 lg:order-1">

            <div className="px-5 py-3 border-b border-white/10 flex items-center justify-between">

              <div className="flex items-center gap-2 text-sm text-slate-400">
                <Terminal size={17} />
                solution.java
              </div>

              <button className="flex items-center gap-2 px-3 py-1.5 rounded-md bg-green-600 text-sm">
                <Play size={14} />
                Run
              </button>

            </div>

            <div className="p-6 font-mono text-sm text-slate-300">

              <p>
                <span className="text-purple-400">public</span>{' '}
                <span className="text-purple-400">int</span>{' '}
                maxSubArray(int[] nums) {'{'}
              </p>

              <p className="pl-6 text-slate-500">
                // Write your solution
              </p>

              <p className="pl-6">
                <span className="text-purple-400">int</span> max = nums[0];
              </p>

              <p className="pl-6">
                <span className="text-purple-400">return</span> max;
              </p>

              <p>
                {'}'}
              </p>

            </div>

            <div className="border-t border-white/10 px-5 py-4">

              <div className="flex items-center gap-2 text-sm text-slate-400 mb-3">
                <Bug size={16} />
                Console
              </div>

              <p className="text-sm text-green-400">
                ✓ Code executed successfully
              </p>

            </div>

          </div>

          {/* Text */}
          <div className="order-1 lg:order-2">

            <p className="text-indigo-400 font-medium mb-3">
              CODE. RUN. IMPROVE.
            </p>

            <h2 className="text-3xl md:text-4xl font-bold">
              Practice without leaving the platform.
            </h2>

            <p className="mt-5 text-slate-400 leading-relaxed">
              Solve DSA problems in an integrated coding workspace.
              Run your solution, test different cases, and use
              AI-powered feedback to improve your implementation.
            </p>

          </div>

        </div>

      </div>

    </section>
  )
}

export default CodingSection