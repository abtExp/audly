import React, { useState, useEffect } from 'react';
import { Play, Pause, SkipBack, SkipForward, Upload, Mic } from 'lucide-react';

const generateStaticWaveform = (length) => {
  return Array.from({ length }, () => Math.random() * 0.8 + 0.2);
};

const AudioProcessingAppSample = () => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentSource, setCurrentSource] = useState(null);
  const [playbackProgress, setPlaybackProgress] = useState(0);
  const staticWaveform = generateStaticWaveform(50); // Reduced for clarity

  useEffect(() => {
    let interval;
    if (isPlaying) {
      interval = setInterval(() => {
        setPlaybackProgress((prev) => (prev < 100 ? prev + 1 : 0));
      }, 100);
    }
    return () => clearInterval(interval);
  }, [isPlaying]);

  const sources = [
    { name: "Drums", color: "bg-blue-100 text-blue-600" },
    { name: "Vocals", color: "bg-purple-100 text-purple-600" },
    { name: "Guitar", color: "bg-green-100 text-green-600" },
    { name: "Speaker 1", color: "bg-yellow-100 text-yellow-600" },
    { name: "Speaker 2", color: "bg-pink-100 text-pink-600" },
    { name: "Ambient", color: "bg-indigo-100 text-indigo-600" }
  ];

  const transcript = [
    { speaker: "Speaker 1", text: "The quick brown fox jumps over the lazy dog.", color: "bg-yellow-100 text-yellow-600" },
    { speaker: "Speaker 2", text: "How vexingly quick daft zebras jump!", color: "bg-pink-100 text-pink-600" },
    { speaker: "Speaker 1", text: "The five boxing wizards jump quickly.", color: "bg-yellow-100 text-yellow-600" },
    { speaker: "Speaker 2", text: "Jackdaws love my big sphinx of quartz.", color: "bg-pink-100 text-pink-600" },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-light mb-12 text-center text-gray-800">
          Audio Processing Studio
        </h1>
        
        {/* Upload/Record Section */}
        <div className="mb-12 text-center">
          <h2 className="text-2xl font-light mb-6 text-gray-700">Upload or Record Audio</h2>
          <div className="flex justify-center space-x-4">
            <button className="bg-blue-100 hover:bg-blue-200 text-blue-600 px-8 py-3 rounded-full flex items-center transition-all duration-300 shadow-sm hover:shadow-md">
              <Upload className="mr-2 h-5 w-5" /> Upload Audio
            </button>
            <button className="bg-green-100 hover:bg-green-200 text-green-600 px-8 py-3 rounded-full flex items-center transition-all duration-300 shadow-sm hover:shadow-md">
              <Mic className="mr-2 h-5 w-5" /> Record Audio
            </button>
          </div>
        </div>

        {/* Waveform and Playback Controls */}
        <div className="mb-12 bg-white rounded-xl shadow-md p-6">
          <div className="h-40 relative overflow-hidden mb-4">
            <div className="absolute inset-0 flex items-center justify-between">
              {staticWaveform.map((height, index) => (
                <div key={index} className="w-1 h-full flex items-center">
                  <div 
                    className="w-full bg-blue-200 rounded-full"
                    style={{ height: `${height * 100}%` }}
                  >
                    <div 
                      className="w-full bg-blue-500 rounded-full transition-all duration-300 ease-in-out"
                      style={{ 
                        height: `${playbackProgress > (index / staticWaveform.length) * 100 ? '100' : '0'}%`,
                        transition: 'height 0.1s ease-in-out'
                      }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="flex justify-between items-center px-4">
            <div className="text-sm text-gray-600">{(playbackProgress / 100 * 3.45).toFixed(2)}</div>
            <div className="flex space-x-4">
              <button className="text-gray-600 hover:text-blue-600 transition-colors duration-300">
                <SkipBack className="h-6 w-6" />
              </button>
              <button 
                onClick={() => setIsPlaying(!isPlaying)}
                className="bg-blue-100 hover:bg-blue-200 text-blue-600 rounded-full w-12 h-12 flex items-center justify-center shadow-sm hover:shadow-md transition-all duration-300"
              >
                {isPlaying ? <Pause className="h-6 w-6" /> : <Play className="h-6 w-6" />}
              </button>
              <button className="text-gray-600 hover:text-blue-600 transition-colors duration-300">
                <SkipForward className="h-6 w-6" />
              </button>
            </div>
            <div className="text-sm text-gray-600">03:45</div>
          </div>
        </div>

        {/* Audio Sources */}
        <div className="mb-12">
          <h2 className="text-2xl font-light mb-4 text-gray-700">Audio Sources</h2>
          <div className="flex flex-wrap gap-3">
            {sources.map((source) => (
              <button
                key={source.name}
                onClick={() => setCurrentSource(source.name)}
                className={`py-2 px-4 rounded-full text-sm transition-all duration-300 ${source.color} ${
                  currentSource === source.name 
                    ? `shadow-md ${source.color.split(' ')[0].replace('100', '200')}` 
                    : 'hover:shadow-sm'
                }`}
              >
                {source.name}
              </button>
            ))}
          </div>
        </div>

        {/* Transcript */}
        <div>
          <h2 className="text-2xl font-light mb-4 text-gray-700">Transcript</h2>
          {transcript.map((entry, index) => (
            <div key={index} className="mb-4 p-4 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
              <div className={`font-medium mb-1 px-2 py-1 rounded-full inline-block ${entry.color}`}>{entry.speaker}</div>
              <div className="text-sm text-gray-700 mt-2">{entry.text}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AudioProcessingAppSample;