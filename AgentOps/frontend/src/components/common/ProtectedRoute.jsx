import { useEffect, useState } from 'react'
import { Navigate, Outlet } from 'react-router-dom'
import { onAuthStateChanged } from 'firebase/auth'

import { auth } from '../../services/firebase'


function ProtectedRoute() {

  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)


  useEffect(() => {

    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {

      setUser(currentUser)
      setLoading(false)

    })


    return () => unsubscribe()

  }, [])


  // Firebase is checking authentication
  if (loading) {

    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">

        <div className="text-center">

          <div className="
            w-8
            h-8
            border-2
            border-blue-600
            border-t-transparent
            rounded-full
            animate-spin
            mx-auto
          " />

          <p className="mt-3 text-sm text-slate-500">
            Loading...
          </p>

        </div>

      </div>
    )

  }


  // User is not logged in
  if (!user) {
    return <Navigate to="/login" replace />
  }


  // User is authenticated
  return <Outlet />

}


export default ProtectedRoute