import React, { useEffect, useState } from 'react'
import "./professor.css"
import Navbar from "@components/navbar/navbar"
import useAuth from "@hooks/useAuth"
import { useNavigate } from 'react-router-dom';
import Dropfile from '../dropfile/Dropfile';
import { useConfirm } from "material-ui-confirm";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import ProfessorStartLesson from './professorStartLesson';
import Professor_Dashboard from './professor_Dashboard';
import ProfessorMyLessons from './professorMyLessons';

export default function Professor({ navbar_items }) {
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
    const handleMenuDisplay = (selected) => {
        switch (selected) {
            case "Dashboard":
                return (
                    <>
                        <Professor_Dashboard onStartSession={handleStartSession} />
                    </>);

            case "My lessons":
                return (
                    <>
                        <ProfessorMyLessons onStartSession={handleStartSession} />
                    </>);

            case "Students":
                return (
                    <>
                        <ProfessorStartLesson onStartSession={handleStartSession} />
                    </>);
            case "Start session":
                return (
                    <>
                        <ProfessorStartLesson onStartSession={handleStartSession} />
                    </>);

            case "Settings":
                return (
                    <>
                        <ProfessorStartLesson onStartSession={handleStartSession} />
                    </>);


        }
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
        <div>
            <ToastContainer limit={2} />
            <div className='screen'>
                <Navbar navbar_items={navbar_items} onChange={handleChange} selected={selected} onStartSession={handleStartSession} />
                <div className='navbar_filler'></div>
                <div className='main_content'>
                    <div className='header'>
                        <div className='user'>
                            <div>
                                <img src="pdp.jpg" height="56px" width="56px" alt="" />
                            </div>
                            <div className='name_and_info'>
                                <div className='name'>
                                    <span>Dhia Ben Hamouda</span>
                                    <img src="arrow-down.svg" alt="" />
                                </div>
                                <div className='info'>Last login: Today</div>
                            </div>
                        </div>
                        <div className='notification'>
                            <img src="notification.svg" alt="" />
                        </div>
                    </div>
                    <div className='content'>
                        {
                            handleMenuDisplay(selected)
                        }
                    </div>
                    <div className='spacer'></div>
                </div>
            </div>

        </div>
    )
}
