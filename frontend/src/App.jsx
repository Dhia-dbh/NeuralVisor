import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Login from '@components/login/login'
import Register from '@components/register/register'
import {
  createBrowserRouter,
  RouterProvider,
  Navigate 
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate  to="/login" />,
  },
  {
    path: "/login",
    element: <Login />
  },
  {
    path: "/register",
    element: <Register />
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
