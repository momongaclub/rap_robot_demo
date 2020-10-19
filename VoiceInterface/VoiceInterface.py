import speech_recognition as sr
import simpleaudio
import time


def rap_battle():
    return 0

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("何か話して下さい ...")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("識別しています ...")

    try:
        print(r.recognize_google(audio, language='ja-JP'))

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("end")
            break

        if r.recognize_google(audio, language='ja-JP') == "ラップバトル" :
            print('開始')
            wav_obj = simpleaudio.WaveObject.from_wave_file('futta-jazz.wav')
            play_obj = wav_obj.play()
            time.sleep(10)
            voice_obj = simpleaudio.WaveObject.from_wave_file('output_mibayashi_syn.wav')
            play_voice_obj = voice_obj.play()
            # play_voice_obj.wait_done()
            # play_obj.wait_done()
            # 音チョット大きく
            rap_battle()

            # time スタート 終了後バースを生成



    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

