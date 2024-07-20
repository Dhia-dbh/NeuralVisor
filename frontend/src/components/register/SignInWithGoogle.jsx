// src/components/SignInWithGoogle.js
import React, { useEffect } from 'react';

const SignInWithGoogle = () => {
    useEffect(() => {
        /* global google */
        google.accounts.id.initialize({
            client_id: 'YOUR_GOOGLE_CLIENT_ID',
            callback: handleCredentialResponse
        });
        google.accounts.id.renderButton(
            document.getElementById('google-signin-button'),
            { theme: 'outline', size: 'large' }
        );
    }, []);

    const handleCredentialResponse = (response) => {
        console.log('Encoded JWT ID token: ' + response.credential);
        // Handle the response. You can send the token to your server for further processing.
    };

    return <div id="google-signin-button"></div>;
};

export default SignInWithGoogle;
