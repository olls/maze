import sys
import copy


cells = [
  {
    'name': 'path',
    'directions': '',
    'image': ['###',
              '###',
              '###']
  }, {
    'name': 'path',
    'directions': 'down',
    'image': ['###',
              '# #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'down-left',
    'image': ['###',
              '  #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'left',
    'image': ['###',
              '  #',
              '###']
  }, {
    'name': 'path',
    'directions': 'right',
    'image': ['###',
              '#  ',
              '###']
  }, {
    'name': 'path',
    'directions': 'right-down',
    'image': ['###',
              '#  ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'right-down-left',
    'image': ['###',
              '   ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'right-left',
    'image': ['###',
              '   ',
              '###']
  }, {
    'name': 'path',
    'directions': 'up',
    'image': ['# #',
              '# #',
              '###']
  }, {
    'name': 'path',
    'directions': 'up-down',
    'image': ['# #',
              '# #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-down-left',
    'image': ['# #',
              '  #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-left',
    'image': ['# #',
              '  #',
              '###']
  }, {
    'name': 'path',
    'directions': 'up-right',
    'image': ['# #',
              '#  ',
              '###']
  }, {
    'name': 'path',
    'directions': 'up-right-down',
    'image': ['# #',
              '#  ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-right-down-left',
    'image': ['# #',
              '   ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-right-left',
    'image': ['# #',
              '   ',
              '###']
  }, {
    'name': 'start',
    'directions': 'down',
    'image': ['###',
              '#*#',
              '# #']
  }, {
    'name': 'end',
    'directions': 'up',
    'image': ['# #',
              '#$#',
              '###']
  }
]

directions = {
  'up': [0, -1],
  'right': [1, 0],
  'left': [-1, 0],
  'down': [0, 1]
}


def interpret(maze):
  new = []
  for line in maze:
    new.append([])
    for char in line:
      new[-1].append(int(char, 18))

  return new


def render(maze):
  out = ''
  for line in maze:
    row = ['', '', '']
    for cell in line:
      row[0] += ''.join(char * 2 for char in cells[cell]['image'][0])
      row[1] += ''.join(char * 2 for char in cells[cell]['image'][1])
      row[2] += ''.join(char * 2 for char in cells[cell]['image'][2])
    out += row[0] + '\n' + row[1] + '\n' + row[2] + '\n'

  return out


def explore(maze, x, y, visited):
  cell = maze[y][x]
  name = cells[cell]['name']
  dirs = cells[cell]['directions']
  visited.append((x, y))

  if name == 'end':
    return True
  else:
    for exit in dirs.split('-'):
      d = directions[exit]

      nx, ny = x + d[0], y + d[1]
      if (nx, ny) not in visited:
        if explore(maze, nx, ny, visited):
          return True


def main():
  with open(sys.argv[1]) as f:
    maze = f.read().splitlines()

  maze = interpret(maze)

  print(render(maze))
  print(explore(maze, 2, 0, []))


if __name__ == '__main__':
  main()