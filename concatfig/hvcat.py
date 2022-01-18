from PIL import Image


def cat_vertical(img_upper, img_lower):
    """cat_vertical.

    Args:
        img_upper:
        img_lower:
    """
    cated_img = Image.new('RGB',
            (max(img_upper.width, img_lower.width),
                img_upper.height + img_lower.height
            ),
    )
    cated_img.paste(img_upper, (0, 0))
    cated_img.paste(img_lower, (0, img_upper.height))
    return cated_img

def cat_horizontal(img_right, img_left):
    """cat_horizontal.

    Args:
        img_right:
        img_left:
    """
    cated_img = Image.new('RGB',
            (img_right.width + img_left.width,
                max(img_right.height,img_left.height)
            ),
    )
    cated_img.paste(img_left, (0, 0))
    cated_img.paste(img_right, (img_left.width, 0))
    return cated_img


