def get_movie_list():
    movie_list_file = open('movies.txt', 'r')
    movie_list = []
    for m in movie_list_file.read().split(','):
        movie_list.append(m)
    movie_list.pop()
    return movie_list

def print_menu():
    print('COMMAND LINE')
    print('list -   List all movies')
    print('add -    Add a movie')
    print('del -    Delete a movie')
    print('exit -   Exit program')
    print()

def list_movies(movie_list):
    for index, value in enumerate(movie_list, start=1):
        print(f'{index}. {value}')
    print()

def add_movie(movie_list):
    new_movie = input('Movie: ')
    movie_list.append(new_movie)
    write_info_to_file(movie_list)
    print(f'{new_movie} was added.')
    print()

def del_movie(movie_list):
    try:
        movie_index = int(input('Number: ')) - 1
        print(f'{movie_list[movie_index]} was deleted.')
        print()
        movie_list.pop(movie_index)
        write_info_to_file(movie_list)
        return
    except:
        print('Invalid movie number.')
        print()

def write_info_to_file(movie_list):
    new_list_data = ""
    for m in movie_list:
        new_list_data += f'{m},'
    movie_file = open('movies.txt','w')
    movie_file.write(new_list_data)

if __name__ == '__main__':
    print('The Movie List program\n')
    print_menu()
    while True:
        command = input('Command: ').lower()
        movie_list = get_movie_list()
        if command == 'list':
            list_movies(movie_list)
        elif command == 'add':
            add_movie(movie_list)
        elif command == 'del':
            del_movie(movie_list)
        elif command == 'exit':
            print('Bye!')
            exit()
        else:
            print('Not a valid command. Please try again.')