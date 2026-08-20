import { Routes, Route } from 'react-router-dom'

import Landing from './pages/Landing/Landing'
import Login from './pages/Auth/Login'
import Signup from './pages/Auth/Signup'

import AppLayout from './components/layout/AppLayout'
import Dashboard from './pages/Dashboard/Dashboard'
import Practice from './pages/Practice/Practice'
import Problem from './pages/Problem/Problem'
import Progress from './pages/Progress/Progress'       
import Bookmarks from './pages/Bookmarks/Bookmarks'
import Roadmap from './pages/Roadmap/Roadmap'
import A2Z from './pages/A2Z/A2Z'
import MCQ from './pages/MCQ/MCQ'
import Tips from './pages/Tips/Tips'
import Profile from './pages/Profile/Profile'
import Settings from './pages/Settings/Settings'
import AICoach from './pages/AICoach/AICoach'
import InterviewPrep from './pages/InterviewPrep/InterviewPrep'


function App() {
  return (
    <Routes>

      {/* Public */}
      <Route path="/" element={<Landing />} />

      {/* Authentication */}
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />

      {/* Main application */}
      <Route element={<AppLayout />}>

        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/practice" element={<Practice />} />

        <Route path="/ai-coach" element={<AICoach />} />

        <Route path="/roadmap" element={<Roadmap />} />

        <Route path="/mcq" element={<MCQ />} />

        <Route path="/interview" element={<InterviewPrep />} />

        <Route path="/progress" element={<Progress />} />

        <Route path="/bookmarks" element={<Bookmarks />} />

        <Route path="/tips" element={<Tips />} />

        <Route path="/problem/:id" element={<Problem />} />

        <Route path="/a2z" element={<A2Z />} />

        <Route path="/profile" element={<Profile />} />

        <Route path="/settings" element={<Settings />} />

      </Route>

    </Routes>
  )
}

export default App