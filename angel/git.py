from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

git_image_path = "git.png"
image_url = "https://assets.mulearn.org/misc/user.png"
role = "STUDENT"
name = "Aashish Vinu"
institute = "MBCET"
i_area = ["Cybersecurity", "Artificial intelligence" ,"web and mobile app development","Internet of Things", "App development"]
rank = "3"
karma = "1"
avatar = BytesIO(requests.get(image_url).content)
im = Image.open(avatar)
if im.size[0] < 256 or im.size[1] < 256:
    im = im.resize((256, 256))

font_name = "PlusJakartaSans-Medium.ttf"
font2 = "PlusJakartaSans-Bold.ttf"

name_color = "rgb(255, 255, 255)"
karma_color = "rgb(255, 255, 255)"
rank_color = "rgb(15, 136, 255)"
color = "rgb(41, 142, 165)"
ig_color = "rgb(75, 75, 75)"

bigsize = (im.size[0] * 3, im.size[1] * 3)
mask = Image.new("L", bigsize, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(im.size, Image.LANCZOS)
im.putalpha(mask)

im = im.resize((round(im.size[0] * 1.0), round(im.size[1] * 1.0)))

background = Image.open(git_image_path)
draw = ImageDraw.Draw(background)

# Name
font = ImageFont.truetype(font_name, size=45)
draw.text((410, 60), name, fill=name_color, font=font)

# Roles
font = ImageFont.truetype(font2 , size=70)
draw.text((1, 753), role, fill=ig_color, font=font)

# College
font = ImageFont.truetype(font_name, size=30)
if len(institute) > 0:
    draw.text((410, 110), institute, fill=name_color, font=font)

# Area of Interest
start_position = (407, 340)
padding = 10
corner_radius = 4
fill_color = ig_color
current_position = start_position
y = start_position[1]
x = start_position[0]
desired_width = 900

# Calculate the maximum height of all the college name boxes
max_height = max(font.getsize("#" + area)[1] + 2 * padding for area in i_area)

if len(i_area)>3:
    font_size=12
else:
    font_size = 15

for area in i_area:
    text = area

    font = ImageFont.truetype(font_name, size=font_size)
    text_width, text_height = font.getsize(text)
    rectangle_width = text_width + 2 * padding
    rectangle_height = text_height + 2 * padding

    # Check if the box exceeds the desired width
    if x + rectangle_width > desired_width:
        x = start_position[0]
        y += max_height - 10  # Adjust the vertical spacing between rows
        max_height = rectangle_height
    else:
        max_height = max(max_height, rectangle_height)

    # Determine the position of the rectangle
    rectangle_x = x
    rectangle_y = y

    # Draw the rectangular background
    draw.rectangle(
        [(rectangle_x, rectangle_y), (rectangle_x + rectangle_width, rectangle_y + rectangle_height)],
        fill=ig_color,
    )

    # Calculate the coordinates to center the text
    text_x = rectangle_x + (rectangle_width - text_width) // 2
    text_y = rectangle_y + (rectangle_height - text_height) // 2

    draw.text((text_x, text_y), text, fill=name_color, font=font)

    x += rectangle_width + 10

# Karma
x = 410
y = 160
font = ImageFont.truetype(font2, size=50)

offsets = {
    6: (17, 29),
    5: (33, 29),
    4: (47, 29),
    3: (65, 29),
    2: (77, 29),
    1: (85, 29),
}
x_offset, y_offset = offsets.get(len(karma), (0, 0))
draw.multiline_text(
    (x + x_offset, y + y_offset),
    karma,
    fill=karma_color,
    font=font,
    align="left",
)

# Rank
x1 = 650
y1 = 160
r = str(rank)
font = ImageFont.truetype(font2, size=50)
offsets = {
    6: (27, 29),
    5: (43, 29),
    4: (56, 29),
    3: (67, 29),
    2: (85, 29),
    1: (93, 29),
}
x1_offset, y1_offset = offsets.get(len(r), (0, 0))
draw.multiline_text(
    (x1 + x1_offset, y1 + y1_offset),
    r,
    fill=rank_color,
    font=font,
    align="left",
)


git = ["ashishvinu08", "34", "1244", "1412"]  # UserID, Public repositories, Total Commits, Followers
if git:
    followers_color = "rgb(151,151,151)"
    userid_color = "rgb(155,153,255)"
    spacing = 15
    userid = "@" + str(git[0])
    public_repo = str(git[1])
    commits = str(git[2])
    followers = str(git[3])
    font_name = "PlusJakartaSans-Medium.ttf" 
    box_color = (135, 133, 255, 76)  # RGB color with opacity (30%)

    # Draw the rectangular background box for the number of commits
    start_position = (730, 616)
    padding = 10
    current_position = start_position
    y = start_position[1]
    x = start_position[0]
    font = ImageFont.truetype(font_name, size=26)
    commit_width, commit_height = font.getsize(commits)
    commit_box_width = commit_width + 2 * padding
    commit_box_height = commit_height + 2 * padding
    
    draw.rectangle(
        [(x,y), (x + commit_box_width,y + commit_box_height)],
        fill=box_color,
    )

    text_x = x + (commit_box_width - commit_width) // 2
    text_y = y + (commit_box_height - commit_height) // 2

    draw.text((text_x, text_y), commits, fill=name_color, font=font)
    
  
    # Draw the rectangular background box for the number of repositories
    start_position = (430, 616)
    padding = 10
    corner_radius = 15
    current_position = start_position
    y = start_position[1]
    x = start_position[0]
    font = ImageFont.truetype(font_name, size=26)
    repo_width, repo_height = font.getsize(public_repo)
    repo_box_width = repo_width + 2 * padding
    repo_box_height = repo_height + 2 * padding
    
    draw.rectangle(
        [(x,y), (x + repo_box_width,y + repo_box_height)],
        fill=box_color,
    )

    text_x = x + (repo_box_width - repo_width) // 2
    text_y = y + (repo_box_height - repo_height) // 2

    draw.text((text_x, text_y), public_repo, fill=name_color, font=font)
    
    # Draw name
    font = ImageFont.truetype(font_name, size=32)
    draw.text((160, 520), name, fill=name_color, font=font)

    # Draw the text for the user ID
    font = ImageFont.truetype(font_name, size=30)
    draw.text((160, 560), userid, fill=userid_color, font=font)

    # Draw followers
    x1 = 600
    y1 = 517
    f = str(followers)
    font = ImageFont.truetype(font_name, size=40)
    offsets = {
        4: (0, 0),
        3: (10, 0),
        2: (22, 0),
        1: (32, 0),
    }
    x1_offset, y1_offset = offsets.get(len(f), (0, 0))
    draw.multiline_text(
        (x1 + x1_offset, y1 + y1_offset),
        f,
        fill=name_color,
        font=font,
        align="left",
    )

background.paste(im, (85, 130), im)
background.show()
