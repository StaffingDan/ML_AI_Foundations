paintings = [
  'The Two Fridas',
  'My Dress Hangs Here',
  'Tree of Hope',
  'Self Portrait With Monkeys'
]

dates = [
  1939,
  1933,
  1946,
  1940
]

data = list(zip(paintings, dates))
data.append([('The Broken Column', 1944), ('The Wounded Deer', 1946), ('Me and My Doll', 1937)])

print(data)
print('There are', len(data), 'Paintings')

audio_tour_numbers = list(range(1, len(data) + 1))
print(audio_tour_numbers)

master_list = list(zip(data, audio_tour_numbers))

print(master_list)
