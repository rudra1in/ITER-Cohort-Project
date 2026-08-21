import { Code2 } from 'lucide-react'
import { Link } from 'react-router-dom'

function AuthLayout({ children }) {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 flex">

      {/* Brand panel */}
      <div className="hidden lg:flex lg:w-[46%] bg-white border-r border-slate-200 items-center justify-center px-12">

        <div className="max-w-md">

          <Link
            to="/"
            className="inline-flex items-center gap-2 mb-12"
          >
            <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center shadow-sm">
              <Code2 size={21} />
            </div>

            <span className="text-xl font-bold tracking-tight">
              DSA Coach
            </span>
          </Link>

          <div className="inline-flex items-center px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-sm font-medium mb-5">
            AI-powered DSA learning
          </div>

          <h1 className="text-4xl font-bold tracking-tight leading-tight">
            Learn DSA by
            <span className="text-blue-600">
              {' '}thinking,
            </span>
            <br />
            not memorizing.
          </h1>

          <p className="mt-5 text-slate-500 text-lg leading-relaxed">
            Practice problems, get progressive hints, understand
            your mistakes, and improve your problem-solving skills
            with your AI DSA Coach.
          </p>

          <div className="mt-8 space-y-4">

            {[
              'Personalized AI guidance',
              'Interactive coding practice',
              'Progress tracking'
            ].map((item) => (
              <div
                key={item}
                className="flex items-center gap-3"
              >
                <div className="w-5 h-5 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center text-xs">
                  ✓
                </div>

                <span className="text-sm text-slate-600">
                  {item}
                </span>
              </div>
            ))}

          </div>

        </div>

      </div>


      {/* Right panel */}
      <div className="w-full lg:w-[54%] min-h-screen flex flex-col">

        {/* Form area */}
        <div className="flex-1 flex items-center justify-center px-6 py-12">

          <div className="w-full max-w-md">

            {/* Mobile logo */}
            <Link
              to="/"
              className="lg:hidden flex items-center justify-center gap-2 mb-10"
            >
              <div className="w-9 h-9 rounded-xl bg-blue-600 text-white flex items-center justify-center">
                <Code2 size={19} />
              </div>

              <span className="text-xl font-bold">
                DSA Coach
              </span>
            </Link>

            {children}

          </div>

        </div>


        {/* Footer */}
        <div className="pb-8 text-center">

          <p className="text-xs text-slate-400">
            © 2026 DSA Coach · Built by Team AgentOps
          </p>

        </div>

      </div>

    </div>
  )
}

export default AuthLayout