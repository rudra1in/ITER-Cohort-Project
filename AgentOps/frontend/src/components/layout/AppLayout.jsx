import { Outlet } from 'react-router-dom'
import Sidebar from './Sidebar'
import TopNavbar from './TopNavbar'

function AppLayout() {

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">

      <Sidebar />

      <div className="lg:ml-64 min-h-screen">

        <TopNavbar />

        <main className="p-6 lg:p-8">
          <Outlet />
        </main>

      </div>

    </div>
  )
}

export default AppLayout