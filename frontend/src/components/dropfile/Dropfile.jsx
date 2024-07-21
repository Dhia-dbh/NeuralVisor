import DropFileInput from './DropFileInput.jsx';
import "./Dropfile.css"

function Dropfile() {
	const onFileChange = (files) => {
		console.log(files);
	}
	return (
		<div className="box">
			<h2 className="header">
				React drop files input
			</h2>
			<DropFileInput
				onFileChange={(files) => onFileChange(files)}
			/>
			<div className='drop_file_buttons'>
				<button class="button-33" role="button">Show Summary</button>
				<button class="button-33" role="button">Generate Quiz</button>

			</div>
		</div>
	);
}

export default Dropfile;
