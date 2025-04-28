import React from 'react';
import './chat.css';

export default function Chat () {
    return(
        <>
        <div className='chat-container'>
            <ul className='chat-messages'>
                <li>Test</li>
                {/*Displace a list of chat history*/}
            </ul>
            <input className='chat-input' type='text' placeholder='Ask something...'></input>
        </div>
        </>
    )
}