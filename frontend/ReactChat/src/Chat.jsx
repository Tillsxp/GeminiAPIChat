import { useState} from 'react';
import axios from 'axios';
import './chat.css';

export default function Chat () {
    const [message, setMessage] = useState('');
    const [chatHistory, setChatHistory] = useState([]);

    const handleSubmit = async (e) =>{
        e.preventDefault();
        try{
            const res = await axios.post('http://localhost:8000/chat', {
                message: message
            });
            setChatHistory(prev => [
                ...prev,
                {role: 'user', text: message},
                {role: 'bot', text: res.data.response},
            ]);
            setMessage('');
        }catch(err){
            console.log(err);
        }
    }

    return(
        <>
        <div className='chat-container'>
            <form onSubmit={handleSubmit}>
            <ul className='chat-messages'>
                {chatHistory.map((msg, index) => (
                    <li key={index} className={msg.role === 'user' ? 'user-message' : 'bot-message'}>
                        <strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.text}
                    </li>
                ))}
            </ul>
            <input className='chat-input' value={message} onChange={(e) => setMessage(e.target.value)} type='text' placeholder='Ask something...'></input>
            <button type='submit' className='chat-send-button'>Send</button>
            </form>
        </div>
        </>
    )
}