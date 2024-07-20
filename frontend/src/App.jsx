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
    path: "/dashboard",
    icon: "navbar/Dashboard",
    name: "Dashboard"
  },
  {
    path: "/mylessons",
    icon: "navbar/My lessons",
    name: "My lessons"
  },
  {
    path: "/students",
    icon: "navbar/Students",
    name: "Students"
  },
  {
    path: "/startseesion",
    icon: "navbar/Start session",
    name: "Start session"
  },
  {
    path: "/settings",
    icon: "navbar/Settings",
    name: "Settings"
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
