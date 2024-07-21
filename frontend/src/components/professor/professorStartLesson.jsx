import React, { useEffect } from 'react'
import Navbar from '../navbar/navbar'
import Dropfile from '../dropfile/Dropfile';
export default function professorStartLesson({ onStartSession }) {
    useEffect(() => {
        // Set overflow styles when component mounts
        document.body.style.overflow = 'hidden';
        document.documentElement.style.overflow = 'hidden';
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Optional: 'smooth' for smooth scrolling, 'auto' for instant
        });

        // Clean up styles when component unmounts
        return () => {
            document.body.style.overflow = 'scroll';
            document.documentElement.style.overflow = 'scroll';
        }
    }, []);
    return (
        <>
            <h2>Live Stream 7/20/2024</h2>
            <div className='grid'>
                <img src="Webcam.png" alt="Webcam" />
                <button type="button" className='btn btn-outline-secondary' onClick={onStartSession} >Start Session</button>
            </div>

        </>
    )
}
