import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import {
  Mail,
  Lock,
  Eye,
  EyeOff,
  ArrowRight
} from 'lucide-react'

import {
  signInWithEmailAndPassword,
  GoogleAuthProvider,
  GithubAuthProvider,
  signInWithPopup
} from 'firebase/auth'

import { auth } from '../../services/firebase'

import AuthLayout from '../../components/common/AuthLayout'
import SocialAuth from '../../components/common/SocialAuth'
import AuthDivider from '../../components/common/AuthDivider'


function Login() {

  const navigate = useNavigate()

  const [showPassword, setShowPassword] = useState(false)

  const [formData, setFormData] = useState({
    email: '',
    password: ''
  })

  const [loading, setLoading] = useState(false)

  const [error, setError] = useState('')


  // =========================================
  // INPUT CHANGE
  // =========================================

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })

    // Remove previous error when user starts typing again
    if (error) {
      setError('')
    }
  }


  // =========================================
  // EMAIL / PASSWORD LOGIN
  // =========================================

  const handleSubmit = async (e) => {

    e.preventDefault()

    setError('')
    setLoading(true)

    try {

      const result = await signInWithEmailAndPassword(
        auth,
        formData.email,
        formData.password
      )

      console.log('Logged in user:', result.user)

      // For now, go directly to dashboard
      navigate('/dashboard')

    } catch (error) {

      console.error('Login error:', error)

      switch (error.code) {

        case 'auth/invalid-credential':
          setError('Invalid email or password.')
          break

        case 'auth/user-not-found':
          setError('No account found with this email.')
          break

        case 'auth/wrong-password':
          setError('Incorrect password.')
          break

        case 'auth/invalid-email':
          setError('Please enter a valid email address.')
          break

        case 'auth/too-many-requests':
          setError(
            'Too many failed attempts. Please try again later.'
          )
          break

        default:
          setError('Unable to sign in. Please try again.')
      }

    } finally {

      setLoading(false)

    }
  }


  // =========================================
  // GOOGLE LOGIN
  // =========================================

  const handleGoogleLogin = async () => {

    setError('')
    setLoading(true)

    try {

      const provider = new GoogleAuthProvider()

      const result = await signInWithPopup(
        auth,
        provider
      )

      console.log('Google user:', result.user)

      navigate('/dashboard')

    } catch (error) {

      console.error('Google login error:', error)

      if (error.code !== 'auth/popup-closed-by-user') {
        setError('Google sign-in failed. Please try again.')
      }

    } finally {

      setLoading(false)

    }
  }


  // =========================================
  // GITHUB LOGIN
  // =========================================

  const handleGithubLogin = async () => {

    setError('')
    setLoading(true)

    try {

      const provider = new GithubAuthProvider()

      const result = await signInWithPopup(
        auth,
        provider
      )

      console.log('GitHub user:', result.user)

      navigate('/dashboard')

    } catch (error) {

      console.error('GitHub login error:', error)

      if (error.code !== 'auth/popup-closed-by-user') {
        setError('GitHub sign-in failed. Please try again.')
      }

    } finally {

      setLoading(false)

    }
  }


  return (

    <AuthLayout>

      {/* ========================================= */}
      {/* HEADING */}
      {/* ========================================= */}

      <div className="mb-8">

        <h2 className="text-3xl font-bold tracking-tight">
          Welcome back
        </h2>

        <p className="mt-2 text-slate-500">
          Continue your DSA learning journey.
        </p>

      </div>


      {/* ========================================= */}
      {/* SOCIAL AUTH */}
      {/* ========================================= */}

      <SocialAuth
        onGoogle={handleGoogleLogin}
        onGithub={handleGithubLogin}
      />


      <AuthDivider />


      {/* ========================================= */}
      {/* ERROR */}
      {/* ========================================= */}

      {error && (

        <div className="
          mb-5
          rounded-xl
          border
          border-red-200
          bg-red-50
          px-4
          py-3
          text-sm
          text-red-600
        ">

          {error}

        </div>

      )}


      {/* ========================================= */}
      {/* EMAIL LOGIN FORM */}
      {/* ========================================= */}

      <form
        onSubmit={handleSubmit}
        className="space-y-5"
      >

        {/* Email */}

        <div>

          <label className="block text-sm font-medium mb-2">
            Email
          </label>

          <div className="relative">

            <Mail
              size={18}
              className="
                absolute
                left-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
              "
            />

            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="you@example.com"
              required
              disabled={loading}
              className="
                w-full
                h-12
                rounded-xl
                border border-slate-200
                bg-white
                pl-11
                pr-4
                text-sm
                outline-none
                transition
                placeholder:text-slate-400
                focus:border-blue-500
                focus:ring-4
                focus:ring-blue-500/10
                disabled:opacity-60
              "
            />

          </div>

        </div>


        {/* Password */}

        <div>

          <div className="flex items-center justify-between mb-2">

            <label className="text-sm font-medium">
              Password
            </label>

            <button
              type="button"
              className="
                text-sm
                text-blue-600
                hover:text-blue-700
              "
            >
              Forgot password?
            </button>

          </div>


          <div className="relative">

            <Lock
              size={18}
              className="
                absolute
                left-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
              "
            />


            <input
              type={showPassword ? 'text' : 'password'}
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Enter your password"
              required
              disabled={loading}
              className="
                w-full
                h-12
                rounded-xl
                border border-slate-200
                bg-white
                pl-11
                pr-11
                text-sm
                outline-none
                transition
                placeholder:text-slate-400
                focus:border-blue-500
                focus:ring-4
                focus:ring-blue-500/10
                disabled:opacity-60
              "
            />


            <button
              type="button"
              disabled={loading}
              onClick={() => setShowPassword(!showPassword)}
              className="
                absolute
                right-3.5
                top-1/2
                -translate-y-1/2
                text-slate-400
                hover:text-slate-600
                transition
                disabled:opacity-50
              "
            >

              {showPassword
                ? <EyeOff size={18} />
                : <Eye size={18} />
              }

            </button>

          </div>

        </div>


        {/* ========================================= */}
        {/* SUBMIT */}
        {/* ========================================= */}

        <button
          type="submit"
          disabled={loading}
          className="
            w-full
            h-12
            rounded-xl
            bg-blue-600
            hover:bg-blue-700
            disabled:bg-blue-400
            text-white
            font-semibold
            flex
            items-center
            justify-center
            gap-2
            transition
            shadow-sm
            hover:shadow-md
            disabled:cursor-not-allowed
          "
        >

          {loading
            ? 'Signing in...'
            : 'Sign In'
          }

          {!loading && (
            <ArrowRight size={18} />
          )}

        </button>

      </form>


      {/* ========================================= */}
      {/* SIGNUP */}
      {/* ========================================= */}

      <p className="mt-7 text-center text-sm text-slate-500">

        Don't have an account?{' '}

        <Link
          to="/signup"
          className="
            font-semibold
            text-blue-600
            hover:text-blue-700
          "
        >
          Create one
        </Link>

      </p>

    </AuthLayout>
  )
}


export default Login