import React, { useEffect, useState } from 'react'
import "./professor.css"
import Navbar from "@components/navbar/navbar"
import useAuth from "@hooks/useAuth"
import { useNavigate } from 'react-router-dom';
import Dropfile from '../dropfile/Dropfile';
import { useConfirm } from "material-ui-confirm";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

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
                <Navbar navbar_items={navbar_items} onChange={handleChange} selected={selected} />
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
                        <h2>Live Stream 7/20/2024</h2>
                        <div className='grid'>
                            <img src="Webcam.png" alt="Webcam" />
                            <button type="button" className='btn btn-outline-secondary' onClick={handleStartSession} >Start Session</button>
                        </div>
                    </div>
                    <div className='spacer'></div>
                    <Dropfile />
                </div>
            </div>

        </div>
    )
}
