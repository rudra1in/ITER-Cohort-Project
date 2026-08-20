import { Bot, CheckCircle2 } from 'lucide-react'

function AICoach() {
  return (
    <section
      id="ai-coach"
      className="py-24 px-6 bg-slate-900/40"
    >

      <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-14 items-center">

        {/* Text */}
        <div>

          <div className="w-12 h-12 rounded-xl bg-indigo-500/10 text-indigo-400 flex items-center justify-center mb-6">
            <Bot size={25} />
          </div>

          <p className="text-indigo-400 font-medium mb-3">
            YOUR AI COACH
          </p>

          <h2 className="text-3xl md:text-4xl font-bold">
            Don't just get the answer.
            <span className="text-indigo-400">
              {' '}Learn how to find it.
            </span>
          </h2>

          <p className="mt-5 text-slate-400 leading-relaxed">
            The AI Coach is designed to guide your thinking.
            Instead of immediately revealing the solution,
            it can provide progressive hints, explain concepts,
            analyze your approach, and help you identify mistakes.
          </p>

          <div className="mt-8 space-y-4">

            {[
              'Progressive hints',
              'Approach explanations',
              'Code error analysis',
              'Personalized feedback'
            ].map((item) => (

              <div
                key={item}
                className="flex items-center gap-3"
              >
                <CheckCircle2
                  size={19}
                  className="text-indigo-400"
                />

                <span className="text-slate-300">
                  {item}
                </span>
              </div>

            ))}

          </div>

        </div>

        {/* Chat Preview */}
        <div className="rounded-xl border border-white/10 bg-slate-950 overflow-hidden">

          <div className="px-5 py-4 border-b border-white/10 flex items-center gap-3">

            <div className="w-9 h-9 rounded-lg bg-indigo-500/10 flex items-center justify-center">
              <Bot size={19} className="text-indigo-400" />
            </div>

            <div>
              <p className="font-medium">
                DSA Coach
              </p>

              <p className="text-xs text-slate-500">
                AI Assistant
              </p>
            </div>

          </div>

          <div className="p-5 space-y-5">

            <div className="bg-slate-900 rounded-lg p-4 max-w-[85%]">
              <p className="text-sm text-slate-300">
                What approach are you thinking of for this problem?
              </p>
            </div>

            <div className="bg-indigo-600 rounded-lg p-4 max-w-[85%] ml-auto">
              <p className="text-sm">
                I think I can solve it using nested loops.
              </p>
            </div>

            <div className="bg-slate-900 rounded-lg p-4 max-w-[85%]">
              <p className="text-sm text-slate-300">
                Good start. Can you think of a way to avoid
                checking every pair?
              </p>
            </div>

          </div>

        </div>

      </div>

    </section>
  )
}

export default AICoach