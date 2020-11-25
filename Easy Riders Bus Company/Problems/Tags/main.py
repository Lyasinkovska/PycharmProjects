import re


template = r'^<[a-z]{1,}?>[\w]{0,}<\/+[a-z]{1,}?\Z>'  # r'^<[a-z]+>.*?<\/{1}[a-z]+>\Z'