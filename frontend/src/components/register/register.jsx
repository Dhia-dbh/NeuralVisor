import React, { useState } from 'react'
import SignInWithGoogle from '@components/register/SignInWithGoogle';
import "./register.css"
export default function Login() {
    const [isPupilSelected, setIsPupilSelected] = useState(true);
    const handleSelectionChange = (newSelection) => {
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
                <div className='title'>Register</div>
                <div className='content'>
                    <div className='type_selection'>
                        <span className={isPupilSelected ? "selected" : ""} onClick={() => handleSelectionChange("Pupil")}>Pupil</span>
                        <span className={!isPupilSelected ? "selected" : ""} onClick={() => handleSelectionChange("Teacher")}>Teacher</span>
                    </div>
                    <div className='form'>
                        <form action="">
                            <input placeholder='Email' type="email" name="email" id="email" />
                            <input placeholder='Username' type="text" name="username" id="username" />
                            <input placeholder='Password' type="password" name="password" id="password" />
                            <input placeholder='Confirm Password' type="password" name="passwordConfirmation" id="passwordConfirmation" />
                            <div className='login_buttons'>
                                <input type="button" value="Sign up" className='btn btn-primary' />
                                <SignInWithGoogle />
                                <div className='no_account'>Already have an account ? <a href="/login">Click here</a></div>

                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}
