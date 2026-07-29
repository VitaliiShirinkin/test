from pathlib import Path
import subprocess

ASSETS = Path("/opt/cursor/artifacts/assets")
TMP = Path("/tmp/perekatchiki-motion")
TMP.mkdir(parents=True, exist_ok=True)

CREAM = "&H00D8EAF1"
BLACK = "&H00050505"
RED = "&H00231BE5"
GREEN = "&H0068774D"
MUSTARD = "&H0035B7EF"

HEADER = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1350
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HeavyCream,Inter,67,{CREAM},{CREAM},{BLACK},&H78050505,-1,0,0,0,100,100,-2,0,1,2,0,7,70,70,70,1
Style: HeavyBlack,Inter,67,{BLACK},{BLACK},{CREAM},&H78F1EAD8,-1,0,0,0,100,100,-2,0,1,1,0,7,70,70,70,1
Style: BoxCream,Inter,54,{CREAM},{CREAM},{BLACK},&H9A050505,-1,0,0,0,100,100,-1,0,3,12,0,7,70,70,70,1
Style: BoxBlack,Inter,52,{BLACK},{BLACK},{CREAM},&H10F1EAD8,-1,0,0,0,100,100,-1,0,3,12,0,7,70,70,70,1
Style: RedLabel,Inter,53,{CREAM},{CREAM},{RED},&H00231BE5,-1,0,0,0,100,100,-1,0,3,12,0,7,70,70,70,1
Style: SerifBlack,Noto Serif,48,{BLACK},{BLACK},{CREAM},&H10F1EAD8,-1,0,0,0,100,100,0,0,1,1,0,7,70,70,70,1
Style: SerifCream,Noto Serif,48,{CREAM},{CREAM},{BLACK},&H78050505,-1,0,0,0,100,100,0,0,1,2,0,7,70,70,70,1
Style: MonoBlack,JetBrains Mono,24,{BLACK},{BLACK},{CREAM},&H10F1EAD8,-1,0,0,0,100,100,0,0,1,0,0,7,70,70,70,1
Style: MonoCream,JetBrains Mono,24,{CREAM},{CREAM},{BLACK},&H78050505,-1,0,0,0,100,100,0,0,1,0,0,7,70,70,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ev(start, end, style, text, tags=""):
    return f"Dialogue: 0,{start},{end},{style},,0,0,0,,{{{tags}}}{text}\n"


slides = [
    {
        "bg": "motion-bg-01.png",
        "out": "perekatchiki-motion-01-tv.mp4",
        "duration": 8.0,
        "flicker": True,
        "events": [
            ev(
                "0:00:00.35", "0:00:03.65", "BoxCream",
                "СЕГОДНЯ БЮРО ВПЕРВЫЕ\\NПОКАЗЫВАЕТ",
                r"\fs46\move(122,165,150,165,0,650)\fad(450,500)"
            ),
            ev(
                "0:00:03.15", "0:00:06.80", "RedLabel",
                "КТО УНОСИТ ИХ\\NПО НОЧАМ.",
                r"\fs48\move(520,650,405,650,0,700)\fad(500,650)"
            ),
        ],
    },
    {
        "bg": "motion-bg-02.png",
        "out": "perekatchiki-motion-02-after-sunset.mp4",
        "duration": 10.0,
        "events": [
            ev(
                "0:00:00.30", "0:00:05.60", "HeavyBlack",
                "ПОСЛЕ ЗАКАТА НА ДОРОГЕ\\NМЕЖДУ «ЕЩЁ МОЖНО»\\NИ «УЖЕ ПОЗДНО» ПОЯВЛЯЮТСЯ\\NМАЛЕНЬКИЕ СВЕТЯЩИЕСЯ\\NСУЩЕСТВА.",
                r"\fs52\move(104,175,70,175,0,750)\fad(500,650)\fscx94\fscy94\t(0,650,\fscx100\fscy100)"
            ),
            ev(
                "0:00:05.05", "0:00:09.45", "BoxBlack",
                "ОНИ КАТЯТ ПЕРЕД СОБОЙ\\NКРУГЛЫЕ КЛУБКИ.",
                r"\move(155,725,105,725,0,600)\fad(500,600)"
            ),
        ],
    },
    {
        "bg": "motion-bg-03.png",
        "out": "perekatchiki-motion-03-what-is-inside.mp4",
        "duration": 9.0,
        "events": [
            ev(
                "0:00:00.30", "0:00:04.70", "BoxCream",
                "ПО ДАННЫМ БЮРО,\\NКЛУБКИ СОСТОЯТ ИЗ ШАГОВ,",
                r"\fs45\move(108,145,78,145,0,650)\fad(450,550)"
            ),
            ev(
                "0:00:03.80", "0:00:08.50", "RedLabel",
                "КОТОРЫЕ ЛЮДИ\\NНЕ СДЕЛАЛИ:",
                r"\fs45\move(520,990,405,990,0,650)\fad(450,600)"
            ),
        ],
    },
    {
        "bg": "motion-bg-04.png",
        "out": "perekatchiki-motion-04-unmade-steps.mp4",
        "duration": 8.0,
        "events": [
            ev("0:00:00.35", "0:00:07.55", "HeavyBlack", "НЕ ПОЗВОНИЛИ",
               r"\pos(145,340)\fad(350,550)\fscx80\fscy80\t(0,450,\fscx100\fscy100)"),
            ev("0:00:01.20", "0:00:07.55", "HeavyCream", "НЕ УШЛИ",
               r"\pos(635,430)\fad(350,550)\fscx80\fscy80\t(0,450,\fscx100\fscy100)"),
            ev("0:00:02.05", "0:00:07.55", "HeavyBlack", "НЕ НАЧАЛИ",
               r"\pos(235,725)\fad(350,550)\fscx80\fscy80\t(0,450,\fscx100\fscy100)"),
            ev("0:00:02.90", "0:00:07.55", "HeavyBlack", "НЕ СКАЗАЛИ",
               r"\pos(615,860)\fad(350,550)\fscx80\fscy80\t(0,450,\fscx100\fscy100)"),
            ev("0:00:04.10", "0:00:07.65", "MonoCream", "НЕПРИНЯТОЕ РЕШЕНИЕ ТОЖЕ ЗАНИМАЕТ МЕСТО.",
               r"\move(170,1165,130,1165,0,450)\fad(400,500)"),
        ],
    },
    {
        "bg": "motion-bg-05.png",
        "out": "perekatchiki-motion-05-heavier.mp4",
        "duration": 11.0,
        "events": [
            ev(
                "0:00:00.30", "0:00:04.60", "HeavyBlack",
                "ЧЕМ ДОЛЬШЕ ЧЕЛОВЕК\\NОТКЛАДЫВАЕТ РЕШЕНИЕ,\\NТЕМ ТЯЖЕЛЕЕ СТАНОВИТСЯ\\NЕГО КЛУБОК.",
                r"\move(105,165,70,165,0,650)\fad(450,550)"
            ),
            ev(
                "0:00:04.15", "0:00:07.80", "BoxBlack",
                "НО ПЕРЕКАТЧИКИ НИКОГО НЕ ОСУЖДАЮТ.",
                r"\move(130,1000,90,1000,0,550)\fad(450,550)"
            ),
            ev(
                "0:00:07.25", "0:00:10.55", "RedLabel",
                "ОНИ ВООБЩЕ ОЧЕНЬ МАЛЕНЬКИЕ\\NИ ЗАНЯТЫ РАБОТОЙ.",
                r"\move(390,1135,240,1135,0,550)\fad(450,500)"
            ),
        ],
    },
    {
        "bg": "motion-bg-06.png",
        "out": "perekatchiki-motion-06-one-step.mp4",
        "duration": 9.0,
        "events": [
            ev(
                "0:00:00.30", "0:00:04.85", "HeavyBlack",
                "ИНОГДА ОДИН ИЗ НИХ\\NОСТАНАВЛИВАЕТСЯ РЯДОМ\\NС ЧЕЛОВЕКОМ.",
                r"\move(105,165,70,165,0,650)\fad(450,600)"
            ),
            ev(
                "0:00:04.25", "0:00:08.55", "HeavyCream",
                "И ОСТАВЛЯЕТ ЕМУ\\NОДИН ШАГ — СОВСЕМ\\NКРОШЕЧНЫЙ,\\NИНОГДА ДАЖЕ СМЕШНОЙ.",
                r"\fs38\move(540,965,455,965,0,650)\fad(500,550)"
            ),
        ],
    },
    {
        "bg": "motion-bg-07.png",
        "out": "perekatchiki-motion-07-enough.mp4",
        "duration": 5.5,
        "events": [
            ev(
                "0:00:00.35", "0:00:04.65", "HeavyBlack",
                "БОЛЬШОГО ДЛЯ НАЧАЛА\\NНЕ ТРЕБУЕТСЯ.",
                r"\fs48\move(500,410,370,410,0,650)\fad(500,600)\fscx92\fscy92\t(0,550,\fscx100\fscy100)"
            ),
        ],
    },
    {
        "bg": "motion-bg-08.png",
        "out": "perekatchiki-motion-08-question.mp4",
        "duration": 10.0,
        "events": [
            ev(
                "0:00:00.30", "0:00:05.70", "HeavyBlack",
                "ЕСЛИ СЕГОДНЯ ВАМ ДОСТАЛСЯ\\NТАКОЙ ШАГ —\\NКУДА БЫ ВЫ ЕГО СДЕЛАЛИ?",
                r"\fs52\move(110,180,70,180,0,650)\fad(500,650)"
            ),
            ev(
                "0:00:05.05", "0:00:07.65", "RedLabel",
                "МОЖНО ОТВЕТИТЬ ОДНИМ СЛОВОМ.",
                r"\fs42\move(160,750,95,750,0,500)\fad(450,500)"
            ),
            ev(
                "0:00:07.10", "0:00:09.70", "SerifBlack",
                "Бюро неучтённых явлений регистрирует\\Nмаленькие аномалии, о которых больше\\Nнекому рассказать.",
                r"\fs33\move(120,895,75,895,0,500)\fad(450,450)"
            ),
            ev(
                "0:00:07.55", "0:00:09.75", "MonoBlack",
                "#БЮРОНЕУЧТЁННЫХЯВЛЕНИЙ  #ДЕЛО001",
                r"\pos(75,1115)\fad(400,400)"
            ),
        ],
    },
]


def make_ass(index, item):
    ass_path = TMP / f"slide-{index:02}.ass"
    ass_path.write_text(HEADER + "".join(item["events"]), encoding="utf-8")
    return ass_path


for index, item in enumerate(slides, start=1):
    ass = make_ass(index, item)
    background = ASSETS / item["bg"]
    output = ASSETS / item["out"]
    duration = item["duration"]
    fade_out = max(duration - 0.28, 0)
    motion = (
        "zoompan="
        "z='min(zoom+0.00010,1.022)':"
        "x='iw/2-(iw/zoom/2)+4*sin(on/55)':"
        "y='ih/2-(ih/zoom/2)+3*cos(on/63)':"
        "d=1:s=1080x1350:fps=30"
    )
    filters = [motion]
    if item.get("flicker"):
        filters.append("eq=brightness='0.008*sin(10*t)'")
        filters.append("noise=alls=2:allf=t")
    filters.append(
        f"subtitles='{ass.as_posix()}':"
        "fontsdir='/usr/share/fonts/truetype/macos'"
    )
    filters.append("fade=t=in:st=0:d=0.20")
    filters.append(f"fade=t=out:st={fade_out:.2f}:d=0.28")
    filters.append("format=yuv420p")
    command = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-framerate", "30",
        "-i", str(background),
        "-t", str(duration),
        "-vf", ",".join(filters),
        "-an",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-movflags", "+faststart",
        str(output),
    ]
    subprocess.run(command, check=True)
    print(f"Rendered {output.name}")
