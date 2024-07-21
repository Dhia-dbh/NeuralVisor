import DropFileInput from './DropFileInput.jsx';
import "./Dropfile.css"

function Dropfile() {
	const onFileChange = (files) => {
		console.log(files);
	}
	return (
		<div className="box">
			<h4 className="header">
				Drop Course Material
			</h4>
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
