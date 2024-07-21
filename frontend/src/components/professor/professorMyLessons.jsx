import React, { useEffect } from 'react'
import Navbar from '../navbar/navbar'
import Dropfile from '../dropfile/Dropfile';
export default function ProfessorMyLessons() {
    useEffect(() => {
        // Set overflow styles when component mounts
        document.body.style.overflow = 'visible';
        document.documentElement.style.overflow = 'visible';
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Optional: 'smooth' for smooth scrolling, 'auto' for instant
        });
    }, []);
    return (
        <>
            <Dropfile />
        </>
    )
}
