import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Login from '@components/login/login'
import Register from '@components/register/register'
import Home from '@components/home/home'
import Professor from '@components/professor/professor'
import NotFound from '@components/not-found/not-found'
import {
  createBrowserRouter,
  RouterProvider,
  Navigate
} from "react-router-dom";
import useAuth from "@hooks/useAuth";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'
import RequireAuth from './components/requireAuth'
import { ConfirmProvider } from 'material-ui-confirm'
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
  {
    path: "/logout",
    icon: "navbar/logout",
    name: "Log Out"
  },
]
const router = createBrowserRouter([

  {
    path: "/home",
    element: <Home />
  },
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
    path: "/",
    element: <RequireAuth />,
    children: [
      {
        path: "/professor",
        element: <Professor navbar_items={navbar_items} />
      },
      {
        path: "/notfound",
        element: <NotFound />,
      },
      {
        path: "/*",
        element: <Navigate to="/notfound" />,
      },
    ]
  }

]);



function App() {
  const { auth, setAuth } = useAuth();

  return (
    <>
      <ConfirmProvider>
        <RouterProvider router={router} />
      </ConfirmProvider>
    </>
  )
}

export default App
