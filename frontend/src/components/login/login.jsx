import React, { useState } from 'react'
import { useNavigate } from "react-router-dom"
import "./login.css"
import { redirectDocument } from 'react-router-dom';
export default function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const handleChange = (e) => {
        switch (e.target.name) {
            case "username":
                setUsername(e.target.value);
                break;
            case "password":
                setPassword(e.target.value);
                break;
        }
    }
    const [isPupilSelected, setIsPupilSelected] = useState(true);
    const handleSelectionChange = (newSelection) => {
        setPassword("");
        if (newSelection === "Pupil") {
            setIsPupilSelected(true);
        }
        else {
            setIsPupilSelected(false);
        }
    }
    return (
        <div className='bg-default'>

            <img src="shredded circle.svg" alt="upper-left-circle" id='upper-left-circle' />
            <img src="left circle.svg" alt="left-circle" id='left-circle' />
            <img src="bottom right triangles.svg" alt="bottom-right-triangles" id='bottom-right-triangles' />
            <div className='main'>
                <div className='title'>Login</div>
                <div className='content'>
                    <div className='type_selection'>
                        <span className={isPupilSelected ? "selected" : ""} onClick={() => handleSelectionChange("Pupil")}>Pupil</span>
                        <span className={!isPupilSelected ? "selected" : ""} onClick={() => handleSelectionChange("Teacher")}>Teacher</span>
                    </div>
                    <div className='form-login'>
                        <form action="">
                            <input placeholder='Username' type="text" name="username" id="username" onChange={handleChange} value={username} />
                            <input placeholder='Password' type="password" name="password" id="password" onChange={handleChange} value={password} />
                            <div className='login_buttons'>
                                <input type="submit" value="Login" className='btn btn-primary' />
                                <div className='no_account'>You don't have an account ? <span className='link-like' onClick={() => {
                                    navigate("/register")
                                }}>Click here</span></div>
                                <div className='goToHome'> <span className='link-like' onClick={() => {
                                    navigate("/professor")
                                }}>SKIP LOGIN</span></div>

                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}
