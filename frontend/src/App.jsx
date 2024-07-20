import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Login from '@components/login/login'
import Register from '@components/register/register'
import Home from '@components/home/home'
import Professor from '@components/professor/professor'
import {
  createBrowserRouter,
  RouterProvider,
  Navigate
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'
const navbar_items = [
  {
    path: "/newpost",
    icon: "",
    name: "New post"
  },
  {
    path: "/conversation",
    icon: "",
    name: "Conversation"
  },
  {
    path: "/newsession",
    icon: "",
    name: "New Session"
  },
  {
    path: "/checkprogress",
    icon: "",
    name: "Check Progress"
  },
  {
    path: "/schedule",
    icon: "",
    name: "Schedule"
  },
  {
    path: "/logout",
    icon: "",
    name: "Log out"
  },
]
const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/home" />,
  },
  {
    path: "/login",
    element: <Login />
  },
  {
    path: "/register",
    element: <Register />
  },
  {
    path: "/professor",
    element: <Professor navbar_items={navbar_items} />
  },
  {
    path: "/home",
    element: <Home />
  },

]);



function App() {


  return (
    <>
      <RouterProvider router={router} />
    </>
  )
}

export default App
