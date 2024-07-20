// src/components/SignInWithGoogle.js
import React, { useEffect } from 'react';

const SignInWithGoogle = () => {
    useEffect(() => {
        /* global google */
        google.accounts.id.initialize({
            client_id: 'Y912231302087-3k88r2m80rmit0mk7nu22fvgp9qg048t.apps.googleusercontent.com',
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
