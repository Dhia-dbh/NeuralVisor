//App.js
import { useState, useEffect } from 'react';
import DropFileInput from './DropFileInput.jsx';
import Quiz from './Quiz.jsx';
import "./dropfile2.css"
function Dropfile() {
	const [quizyes, setquiz] = useState(false)
	const [sumyes, setsum] = useState(false)
	const [summary, setSummary] = useState('');
	const [points, setpoints] = useState([]);
	const showquiz = () => {
		setquiz(true)

	}
	const showSummary = () => {
		setsum(true)
		setSummary('Machine learning is a subset of artificial intelligence. It can analyze large datasets and make data-driven decisions with minimal human intervention. In healthcare, machine learning algorithms are used for predictive analytics. In finance, it aids in fraud detection, risk management, and algorithmic trading.');
		setpoints(["What is machine learning", "How does a machine learn", "What are some real world applications of Machine learning"])
	};
	const onFileChange = (files) => {
		console.log(files);
	}
	useEffect(() => {
		// Set overflow styles when component mounts
		if (summary === '') {
			document.body.style.overflow = 'hidden';
			document.documentElement.style.overflow = 'hidden';
		}
		else {
			document.body.style.overflow = 'scroll';
			document.documentElement.style.overflow = 'scroll';
		}

		// Clean up styles when component unmounts
		return () => {
			document.body.style.overflow = 'hidden';
			document.documentElement.style.overflow = 'hidden';
		}
	}, [summary]);
	return (
		<div className="box">
			<h2 className="header">
				select the file you want to study for today !
			</h2>
			<DropFileInput
				onFileChange={(files) => onFileChange(files)}
			/>
			<div className='drop_file_input_buttons'>
				<button class="button-33" role="button" onClick={showSummary}>Show Summary</button>
				<button class="button-33" role="button" onClick={showquiz}>Generate Quiz</button>
			</div>
			{quizyes && (
				<>
					<Quiz />
				</>
			)}
			{sumyes && ( // Conditionally render content
				<>
					<h2>Here is a quick wrap up of the lesson you apploaded !</h2>
					<h2>Key point </h2>
					<ul>
						{points.map((point, index) => (
							<li key={index}>{point}</li>
						))}
					</ul>
					<h2>Quick summary</h2>
					<p>{summary}</p>

				</>
			)}

		</div>
	);
}

export default Dropfile;
