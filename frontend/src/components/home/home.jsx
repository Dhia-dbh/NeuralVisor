import React, { useEffect } from 'react'
import "./home.css"
import { useNavigate } from 'react-router-dom'
export default function Home() {
    const navigate = useNavigate();
    useEffect(() => {
        // Set overflow styles when component mounts
        document.body.style.overflow = 'hidden';
        document.documentElement.style.overflow = 'hidden';

    }, []);
    return (
        <div style={{ overflow: "hidden" }}>
            <div className='bg-default_home'>
                <img src="bottom right triangles.svg" alt="" className='bottom-right-traingles' />
                <img src="left circle.svg" alt="" className='left-circle' />
                <img src="top shredded circle.svg" alt="" className='top-shredded-circle' />
                <div className='title_home'>WELCOME TO NURALVISOR PLATFORM !</div>
                <div className='subtitle_home' onClick={() => {
                    navigate("/login")
                }}>Let's Get Started</div>
            </div>
        </div>
    )
}
