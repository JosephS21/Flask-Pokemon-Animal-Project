


# @app.route('/user')
# def mycollection():
#     pokemons= Pokemon.query.filter_by(user_id=current_user.id)
#     return render_template ('user.jinja', pokemons=pokemons)

# @app.route('/user/<pokemon_id>/delete')
# def delete_pokemon(pokemon_id):
#     pokemon = Pokemon.query.get(pokemon_id)
#     if current_user.id != pokemon.user_id:
#         flash('This isn\'t your Pokemon!')
#         return redirect(url_for('mycollection'))
#     pokemon.delete_pokemon()
#     flash('Pokemon deleted!')
#     return redirect(url_for('mycollection'))


