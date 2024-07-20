import React from 'react'
import "./login.css"
export default function Login() {
    return (
        <div className='bg-black'>
            <div className='main'>
                <div className='title'>Login</div>
                <div className='content'>
                    <div className='type_selection'>
                        <span>Pupil</span>
                        <span>Teacher</span>
                    </div>
                </div>
                <div className='form'>
                    <form action="">
                        <input type="text" name="username" id="username" />
                        <input type="password" name="password" id="password" />
                        <div className='login_buttons'>
                            <input type="button" value="Login" className='btn btn-primary' />
                            <input type="button" value="Sign in" />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}
