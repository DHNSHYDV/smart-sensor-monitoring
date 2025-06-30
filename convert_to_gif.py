import os
from moviepy.editor import VideoFileClip

def convert_video_to_gif(video_path, output_path, fps=10, scale=0.5):
    """
    Convert a video file to GIF
    
    Args:
        video_path (str): Path to the input video file
        output_path (str): Path to save the output GIF
        fps (int): Frames per second for the output GIF
        scale (float): Scale factor for the output (0-1)
    """
    try:
        print(f"Converting {video_path} to GIF...")
        
        # Load the video file
        video = VideoFileClip(video_path)
        
        # Resize the video
        if scale != 1:
            video = video.resize(scale)
        
        # Write the GIF file
        video.write_gif(
            output_path,
            fps=fps,
            program='ffmpeg',
            opt='optimizeplus',
            fuzz=3
        )
        
        print(f"Successfully created {output_path}")
        return True
        
    except Exception as e:
        print(f"Error converting video to GIF: {str(e)}")
        return False

if __name__ == "__main__":
    # Input and output paths
    input_video = "assets/videos/Screen Recording 2025-06-29 at 11.14.17 AM.mov"
    output_gif = "assets/demo.gif"
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_gif), exist_ok=True)
    
    # Convert video to GIF
    success = convert_video_to_gif(input_video, output_gif, fps=8, scale=0.6)
    
    if success:
        print("\nTo use this GIF in your README, add:")
        print(f"![Demo GIF]({output_gif})")
    else:
        print("\nFailed to convert video to GIF. Please check the error message above.")
