import React, { useState } from 'react'
import "./professor.css"
import Navbar from "@components/navbar/navbar"

export default function Professor({ navbar_items }) {
    const [selected, setSelected] = useState("Start session");
    const handleChange = (menu) => {
        setSelected(menu)
    }
    return (
        <div>
            <div className='screen'>
                <Navbar navbar_items={navbar_items} onChange={handleChange} selected={selected} />
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
                            <button type="button" className='btn btn-outline-secondary' >Start Session</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
