from . import bp as social_bp
from .models import User, Blog, Pokemon
from flask import render_template, flash, redirect, url_for, request
from app.forms import BlogForm, PokemonCatcherForm
from flask_login import login_required, current_user
from random import randint
import requests


@social_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    pokemons= Pokemon.query.filter_by(user_id=current_user.id)
    if not user_match:
        redirect('/')
    blogs= user_match.blogs
    return render_template('user.jinja', user=user_match, blogs=blogs, pokemons=pokemons )

@social_bp.route('/blog', methods=['GET','POST'])
@login_required
def blog():
    form=BlogForm()
    if form.validate_on_submit():
        blogblock=form.blogblock.data
        b=Blog(blogblock=blogblock, user_id=current_user.id) 
        b.commit()
        flash(f'Successfully sent a Blog!')
    return render_template('blog.jinja', blog_form=form)

@social_bp.route('/avaliable', methods=["GET", "POST"])
def avaliable_pokemon():
    form=PokemonCatcherForm()
    if request.method == "POST":
        if form.validate_on_submit():
            pokemon_name = form.pokemon_name.data

            def pokemon_info(p_name):
                response= requests.get(f'https://pokeapi.co/api/v2/pokemon/{p_name}')
                if response.ok:
                    my_pokemon = {}
                    my_pokemon = {'pokemon_name': response.json()['forms'][0]['name'],
                                  'ability': response.json()['abilities'][0]['ability']['name'],
                                  'type': response.json()['types'][0]['type']['name'],
                                  'sprite': response.json()['sprites']['front_default']}
                    return my_pokemon
                    # if not Pokemon.known_pokemon(my_pokemon[pokemon_name]):
                    #     poke=Pokemon()
                    #     poke.commit()
                    # return render_template('user.jinja', my_pokemon=my_pokemon, form=form)
                
            if pokemon_name.lower() == "random":
                a = randint(1,1008)
                b = randint(10001, 10271)
                c = randint(1,1279)
                if c < 1009:
                    pokemon_index = a
                elif c > 1008:
                    pokemon_index= b
                the_pokemon = pokemon_info(pokemon_index)
            else:
                the_pokemon = pokemon_info(pokemon_name.lower())

            if current_user.is_authenticated:

                form.pokemon_name.data= ''

                if the_pokemon:
                    pokemon_name = the_pokemon['pokemon_name'].capitalize()
                    ability= the_pokemon['ability']
                    type= the_pokemon['type']
                    sprite= the_pokemon['sprite']
                    user_id= current_user.id

                    dblist= Pokemon.query.filter_by(pokemon_name = pokemon_name).all()
                    if dblist == []:
                        if len(Pokemon.query.filter_by(user_id= current_user.id).all()) < 5:
                            pokemon= Pokemon(pokemon_name, ability, type, sprite, user_id)
                            pokemon.commit()
                            flash("Pokemon added to your collection!")
                        else:
                            flash("Can't have more then 5 at a time!")
                            return redirect(url_for('social.avaliable_pokemon'))
                    else:
                        flash("That Pokemon already has a trainer.")
                        return redirect(url_for('social.avaliable_pokemon'))
                return render_template('avaliable_pokemon.jinja', form=form, the_pokemon = the_pokemon)
          
    elif request.method=="GET":
        return render_template("avaliable_pokemon.jinja", form=form, title="Find Pokemon")