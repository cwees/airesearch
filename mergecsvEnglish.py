import pandas as pd
import os
from lingua import LanguageDetectorBuilder, Language


def all():
    stuff = [
        "bard",
        "elevenlabs",
        "copilot",
        "jasper",
        "midjourney",
        "openai",
        "stablediffusion",
        "all",
    ]
    for file in stuff:
        merge(file)


def merge(dir):

    file_path = dir + "/"
    file_list = os.listdir(file_path)
    print(file_list)
    df = pd.DataFrame()
    list = []
    for file in file_list:
        temp = pd.read_csv(
            file_path + file,
            lineterminator="\n",
            encoding="utf-8",
            low_memory=False,
        )
        list.append(temp)
        # df = pd.concat([df_temp,df_temp],ignore_index=True,axis=0)
    df = pd.concat(list, ignore_index=True)

    initial = int(df.size / 15)
    # df.drop_duplicates(keep="first", inplace=True)
    df = df[df["TEXT"].apply(detect_eng)]
    final = int(df.size / 15)
    # print(df.head)
    print(f"{dir} initial data size: {initial} English data size: {final}")
    df.to_csv("input\\" + file, index=False)


def detect_eng(text):
    detector = LanguageDetectorBuilder.from_all_languages().build()
    try:
        return detector.detect_language_of(text) == Language.ENGLISH
    except:
        return False


all()
