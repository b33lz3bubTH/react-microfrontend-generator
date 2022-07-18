import React, { useState, useEffect } from "react";
import { formStore } from 'ui';



export const ResearchPage = ({ title }) => {
    const [currentFormState, setCurrentFormState] = useState(null);
    useEffect(() => {
        formStore.subscribe(setCurrentFormState);
        formStore.init();
    }, []);
    const handleFormSubmit = () => {
        formStore.setFormData({
            name: 'Sourav From Research',
            message: 'Message Passed From Research',
            email: 'Sourav A'
        })
    }
    return (
        <div style={{border: '1px dashed red'}}>
            <h1>Research Page: {title}</h1>
            <button onClick={handleFormSubmit}>Submit Data</button>
            <h2 style={{ color: 'red' }}>{JSON.stringify(currentFormState)}</h2>
        </div>
    )
}