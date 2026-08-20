import { Link } from 'react-router-dom'
import { ArrowRight } from 'lucide-react'

function CTA() {
  return (
    <section className="py-24 px-6">

      <div className="max-w-5xl mx-auto">

        <div className="rounded-2xl border border-indigo-500/20 bg-indigo-500/10 p-10 md:p-16 text-center">

          <h2 className="text-3xl md:text-4xl font-bold">
            Ready to become better at DSA?
          </h2>

          <p className="mt-4 text-slate-400 max-w-xl mx-auto">
            Start solving problems with an AI coach
            that helps you think, learn, and improve.
          </p>

          <Link
            to="/signup"
            className="inline-flex items-center gap-2 mt-8 px-6 py-3 rounded-lg bg-indigo-600 hover:bg-indigo-500 transition font-semibold"
          >
            Start Learning
            <ArrowRight size={18} />
          </Link>

        </div>

      </div>

    </section>
  )
}

export default CTA