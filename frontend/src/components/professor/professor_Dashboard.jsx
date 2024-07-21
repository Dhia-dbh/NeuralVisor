import React, { useEffect, useState } from 'react'
import "./professor.css"
import Navbar from "@components/navbar/navbar"
import useAuth from "@hooks/useAuth"
import { useNavigate } from 'react-router-dom';
import Dropfile from '../dropfile/Dropfile';
import { useConfirm } from "material-ui-confirm";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Student from '../student/Student';

export default function Professor_Dahboard({ navbar_items }) {
    const confirm = useConfirm();
    const [selected, setSelected] = useState("Start session");
    const { auth, setAuth } = useAuth();
    const navigate = useNavigate();
    const handleChange = (menu) => {
        if (menu === "Log Out") {
            confirm({ description: `Are You sure you want to Log Out ?` })
                .then(() => {
                    setAuth({});
                    navigate("/");
                })
                .catch(() => console.log("Log Out cancelled."));

        }
        else {
            setSelected(menu)
        }
    }
    const handleStartSession = () => {
        toast.dismiss();
        toast.info("Wow so easy!");
    }
    useEffect(() => {
        // Set overflow styles when component mounts
        document.body.style.overflow = 'scroll';
        document.documentElement.style.overflow = 'scroll';

        // Clean up styles when component unmounts
        return () => {
            document.body.style.overflow = 'hidden';
            document.documentElement.style.overflow = 'hidden';
        }
    }, []);

    return (
        <>
            <Student />
        </>
    )
}
