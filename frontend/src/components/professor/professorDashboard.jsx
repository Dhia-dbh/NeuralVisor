import React, { useEffect } from 'react'
import Navbar from '../navbar/navbar'
import Dropfile from '../dropfile/Dropfile';
export default function ProfessorDashboard({ navbar_items, onChange, selected, onStartSession }) {
    useEffect(() => {
        // Set overflow styles when component mounts
        document.body.style.overflow = 'hidden';
        document.documentElement.style.overflow = 'hidden';

        // Clean up styles when component unmounts
        return () => {
            document.body.style.overflow = 'scroll';
            document.documentElement.style.overflow = 'scroll';
        }
    }, []);
    return (
        <>
            <Navbar navbar_items={navbar_items} onChange={onChange} selected={selected} onStartSession={onStartSession} />
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
                        <button type="button" className='btn btn-outline-secondary' onClick={onStartSession} >Start Session</button>
                    </div>
                </div>
                <div className='spacer'></div>
            </div>
        </>
    )
}
