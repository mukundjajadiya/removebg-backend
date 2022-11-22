from rembg import remove


def removeLocalImageBG(input_path, output_path="output/output.png"):
    with open(input_path, "rb") as i:
        with open(output_path, "wb") as o:
            input = i.read()
            output = remove(input)
            o.write(output)
            return output


def removeImageBG(imageBytes):
    output = remove(imageBytes)
    return output


if __name__ == "__main__":
    removeLocalImageBG(input_path="images/6.JPG")
