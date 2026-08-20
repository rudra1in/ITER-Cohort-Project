import {
  Brain,
  Code2,
  Target,
  TrendingUp,
  Lightbulb,
  MessageSquare
} from 'lucide-react'

const features = [
  {
    icon: Brain,
    title: 'AI-Powered Coaching',
    description:
      'Get guidance while solving problems instead of simply receiving the answer.'
  },
  {
    icon: Lightbulb,
    title: 'Progressive Hints',
    description:
      'Receive hints gradually so you can develop your own problem-solving skills.'
  },
  {
    icon: Code2,
    title: 'Built-in Code Editor',
    description:
      'Write, run, test, and improve your solutions inside the platform.'
  },
  {
    icon: Target,
    title: 'Structured DSA Practice',
    description:
      'Practice problems organized by topic, difficulty, and learning progression.'
  },
  {
    icon: TrendingUp,
    title: 'Track Your Progress',
    description:
      'Monitor your solved problems, learning progress, and areas for improvement.'
  },
  {
    icon: MessageSquare,
    title: 'Interactive Feedback',
    description:
      'Understand your mistakes with explanations and actionable feedback.'
  }
]

function Features() {
  return (
    <section
      id="features"
      className="py-24 px-6"
    >

      <div className="max-w-7xl mx-auto">

        <div className="text-center max-w-2xl mx-auto">

          <p className="text-indigo-400 font-medium mb-3">
            FEATURES
          </p>

          <h2 className="text-3xl md:text-4xl font-bold">
            Everything you need to master DSA
          </h2>

          <p className="mt-4 text-slate-400">
            Learn concepts, solve problems, and improve your
            coding skills with an AI coach guiding you along the way.
          </p>

        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mt-14">

          {features.map((feature) => {

            const Icon = feature.icon

            return (
              <div
                key={feature.title}
                className="p-6 rounded-xl border border-white/10 bg-slate-900/60 hover:bg-slate-900 transition"
              >

                <div className="w-11 h-11 rounded-lg bg-indigo-500/10 text-indigo-400 flex items-center justify-center mb-5">
                  <Icon size={22} />
                </div>

                <h3 className="text-lg font-semibold mb-2">
                  {feature.title}
                </h3>

                <p className="text-slate-400 leading-relaxed">
                  {feature.description}
                </p>

              </div>
            )
          })}

        </div>

      </div>

    </section>
  )
}

export default Features
