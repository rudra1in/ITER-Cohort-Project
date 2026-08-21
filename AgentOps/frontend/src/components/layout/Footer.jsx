import { Code2 } from 'lucide-react'

function Footer() {
  return (
    <footer className="border-t border-white/10">

      <div className="max-w-7xl mx-auto px-6 py-10">

        <div className="flex flex-col md:flex-row items-center justify-between gap-5">

          <div className="flex items-center gap-2">

            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center">
              <Code2 size={18} />
            </div>

            <span className="font-semibold">
              DSA Coach
            </span>

          </div>

          <p className="text-sm text-slate-500">
            Learn DSA. Think better. Code smarter.
          </p>

        </div>

      </div>

    </footer>
  )
}

export default Footer