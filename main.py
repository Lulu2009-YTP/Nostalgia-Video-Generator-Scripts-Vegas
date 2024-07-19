import vegas
import random
import os

# Add media sources
def add_media(track, media_path):
    media = vegas.Media(media_path)
    event = vegas.VideoEvent(vegas.Timecode(0), media.Length)
    track.Events.Add(event)
    event.AddTake(media.GetVideoStream())
    return event

# Apply random effects
def apply_random_effects(event):
    effects = [
        "Glow", "Mirror", "Swirl", "Deform", "Wave", "TV Simulator", "Chroma Key"
    ]
    selected_effect = random.choice(effects)
    effect = vegas.Effect(selected_effect)
    event.Effects.Add(effect)

# Main function to create the video
def create_nostalgia_video(output_path):
    vegas.Project.Tracks.Clear()
    
    video_track = vegas.Project.Tracks.AddVideoTrack()
    audio_track = vegas.Project.Tracks.AddAudioTrack()

    media_sources = [
        "path/to/video.mp4",
        "path/to/image.jpg",
        "path/to/audio.mp3",
    ]
    
    for media_path in media_sources:
        if media_path.endswith(('.mp4', '.avi', '.mov')):
            event = add_media(video_track, media_path)
        elif media_path.endswith(('.jpg', '.png', '.gif')):
            event = add_media(video_track, media_path)
        elif media_path.endswith(('.mp3', '.wav')):
            event = add_media(audio_track, media_path)
        
        apply_random_effects(event)
    
    # Render settings
    render_settings = vegas.RenderSettings()
    render_settings.OutputFilePath = output_path
    vegas.Project.Render(render_settings)

if __name__ == "__main__":
    output_video = "path/to/output/video.mp4"
    create_nostalgia_video(output_video)
